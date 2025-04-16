"""
LLM client for RepoInsight.

This module provides functionality for interacting with language models through
OpenAI-compatible APIs, such as Cortex.
"""

import asyncio
import hashlib
import json
import logging
import time
from pathlib import Path
from typing import Any

import aiohttp

logger = logging.getLogger(__name__)


class LLMClient:
    """
    Client for interacting with LLM APIs using the OpenAI-compatible format.

    Supports local model servers like Cortex and cloud services like OpenAI.
    """

    def __init__(
        self,
        base_url: str = "http://localhost:8000/v1",
        api_key: str | None = None,
        timeout: int = 30,
        max_retries: int = 3,
        retry_delay: int = 2,
        cache_dir: str | Path | None = None,
    ) -> None:
        """
        Initialize an LLM client.

        Args:
            base_url: Base URL for the API
            api_key: API key (if required)
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries on failure
            retry_delay: Delay between retries in seconds
            cache_dir: Directory for caching responses
        """
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.cache_dir = Path(cache_dir) if cache_dir else None

        # Create cache directory if specified
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_default_headers(self) -> dict[str, str]:
        """Get default headers for API requests."""
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def _get_cache_path(self, cache_key: str) -> Path | None:
        """Get the cache file path for a given key."""
        if not self.cache_dir:
            return None

        # Create a hash of the key for the filename
        key_hash = hashlib.md5(cache_key.encode()).hexdigest()
        return self.cache_dir / f"{key_hash}.json"

    async def _get_from_cache(self, cache_key: str) -> dict[str, Any] | None:
        """Try to get a response from the cache."""
        if not self.cache_dir:
            return None

        cache_path = self._get_cache_path(cache_key)
        if not cache_path or not cache_path.exists():
            return None

        try:
            with open(cache_path, encoding="utf-8") as f:
                cache_data = json.load(f)

            # Check if the cache has expired (if expiration is set)
            if "expiration" in cache_data and cache_data["expiration"] < time.time():
                # Cache expired
                return None

            return cache_data.get("response")
        except (OSError, json.JSONDecodeError) as e:
            logger.warning(f"Error reading cache: {e}")
            return None

    async def _save_to_cache(
        self, cache_key: str, response: dict[str, Any], ttl: int | None = None
    ) -> None:
        """Save a response to the cache."""
        if not self.cache_dir:
            return

        cache_path = self._get_cache_path(cache_key)
        if not cache_path:
            return

        try:
            cache_data = {
                "response": response,
                "timestamp": time.time(),
            }

            # Add expiration if TTL is provided
            if ttl is not None:
                cache_data["expiration"] = time.time() + ttl

            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f)
        except OSError as e:
            logger.warning(f"Error writing to cache: {e}")

    def _compute_cache_key(
        self, model: str, messages: list[dict[str, str]], additional_key: str | None = None
    ) -> str:
        """Compute a cache key for the request."""
        # Create a dictionary of the request parameters
        key_data = {
            "model": model,
            "messages": messages,
        }

        # Add additional key information if provided
        if additional_key:
            key_data["additional_key"] = additional_key

        # Convert to a consistent string representation
        key_str = json.dumps(key_data, sort_keys=True)

        # Return a hash of the key string
        return hashlib.sha256(key_str.encode()).hexdigest()

    async def chat_completion(
        self,
        model: str,
        messages: list[dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int | None = None,
        top_p: float | None = None,
        frequency_penalty: float | None = None,
        presence_penalty: float | None = None,
        stop: str | list[str] | None = None,
        cache_key: str | None = None,
        use_cache: bool = True,
    ) -> dict[str, Any]:
        """
        Send a chat completion request to the API.

        Args:
            model: Model to use for generation
            messages: List of message objects
            temperature: Sampling temperature (0.0-2.0)
            max_tokens: Maximum number of tokens to generate
            top_p: Nucleus sampling parameter
            frequency_penalty: Frequency penalty parameter
            presence_penalty: Presence penalty parameter
            stop: Stop sequence(s) to end generation
            cache_key: Additional information to include in the cache key
            use_cache: Whether to use cache for this request

        Returns:
            API response as a dictionary
        """
        # Prepare the request payload
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        # Add optional parameters if provided
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if top_p is not None:
            payload["top_p"] = top_p
        if frequency_penalty is not None:
            payload["frequency_penalty"] = frequency_penalty
        if presence_penalty is not None:
            payload["presence_penalty"] = presence_penalty
        if stop is not None:
            payload["stop"] = stop

        # Try to get from cache if enabled
        if use_cache and self.cache_dir:
            computed_cache_key = self._compute_cache_key(model, messages, cache_key)
            cached_response = await self._get_from_cache(computed_cache_key)
            if cached_response:
                logger.debug(f"Cache hit for {computed_cache_key}")
                return cached_response

        # Make the API request with retries
        for attempt in range(self.max_retries):
            try:
                async with aiohttp.ClientSession() as session, session.post(
                    f"{self.base_url}/chat/completions",
                    headers=self._get_default_headers(),
                    json=payload,
                    timeout=self.timeout,
                ) as response:
                    if response.status == 200:
                        result = await response.json()

                        # Save to cache if enabled
                        if use_cache and self.cache_dir:
                            await self._save_to_cache(computed_cache_key, result)

                        return result
                    error_text = await response.text()
                    logger.error(
                        f"API error (attempt {attempt+1}/{self.max_retries}): "
                        f"Status {response.status} - {error_text}"
                    )

                    # If we've exhausted retries, raise an exception
                    if attempt == self.max_retries - 1:
                        response.raise_for_status()
            except (TimeoutError, aiohttp.ClientError) as e:
                logger.error(f"Request error (attempt {attempt+1}/{self.max_retries}): {e}")

                # If we've exhausted retries, re-raise the exception
                if attempt == self.max_retries - 1:
                    raise

            # Wait before retrying
            await asyncio.sleep(self.retry_delay * (2**attempt))  # Exponential backoff

        # This should not be reached if max_retries > 0
        raise RuntimeError("Failed to get a response from the API")

    async def generate_description(
        self,
        file_path: str | Path,
        file_content: str,
        language: str,
        model: str = "llama3",
        temperature: float = 0.3,
        max_tokens: int = 500,
        system_prompt_template: str | None = None,
        commit_hash: str | None = None,
    ) -> str:
        """
        Generate a description for a source code file.

        Args:
            file_path: Path to the file
            file_content: Content of the file
            language: Programming language of the file
            model: Model to use for generation
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum number of tokens to generate
            system_prompt_template: Template for system prompt (with {language} placeholder)
            commit_hash: Git commit hash for cache key

        Returns:
            Generated description as a string
        """
        # Use default system prompt template if not provided
        if system_prompt_template is None:
            system_prompt_template = (
                "Analyze the following {language} code and provide a concise description "
                "in markdown format. Focus on the main purpose, key functionality, and "
                "important patterns or techniques used. Keep the description under 5 sentences."
            )

        # Format the system prompt
        system_prompt = system_prompt_template.format(language=language)

        # Prepare messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": file_content},
        ]

        # Create cache key with commit hash if available
        cache_key = None
        if commit_hash:
            path_str = str(file_path)
            cache_key = f"{path_str}:{commit_hash}"

        try:
            # Make the API request
            response = await self.chat_completion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                cache_key=cache_key,
            )

            # Extract and return the generated description
            if "choices" in response and len(response["choices"]) > 0:
                return response["choices"][0]["message"]["content"].strip()
            
            logger.warning(f"Unexpected response format: {response}")
            return "Error: Unexpected response format from LLM API."
        except Exception as e:
            logger.error(f"Error generating description: {e}")
            return f"Error generating description: {str(e)}"
