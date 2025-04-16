"""
Caching system for LLM responses.

This module provides a filesystem-based caching system for storing and retrieving
LLM responses, optimized for codebase analysis.
"""

import json
import logging
import time
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class CacheManager:
    """
    File-based cache manager for LLM responses.

    Stores responses in JSON files organized by key, with optional
    expiration times for cache invalidation.
    """

    def __init__(self, cache_dir: str | Path) -> None:
        """
        Initialize a cache manager.

        Args:
            cache_dir: Directory to store cache files
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_path(self, key: str) -> Path:
        """
        Get the path to a cache file for a given key.

        Args:
            key: Cache key

        Returns:
            Path to the cache file
        """
        # Create a safe filename from the key
        safe_key = "".join(c if c.isalnum() else "_" for c in key)
        if len(safe_key) > 100:  # Limit filename length
            import hashlib

            # Use part of the original key + hash for uniqueness
            hash_part = hashlib.md5(key.encode()).hexdigest()
            safe_key = f"{safe_key[:50]}_{hash_part}"

        return self.cache_dir / f"{safe_key}.json"

    async def get(self, key: str) -> Any | None:
        """
        Get a value from the cache.

        Args:
            key: Cache key

        Returns:
            Cached value, or None if not found or expired
        """
        cache_path = self._get_cache_path(key)

        if not cache_path.exists():
            return None

        try:
            with open(cache_path, encoding="utf-8") as f:
                cache_data = json.load(f)

            # Check if the cache has expired
            if "expiration" in cache_data and cache_data["expiration"] < time.time():
                logger.debug(f"Cache expired for key: {key}")
                return None

            logger.debug(f"Cache hit for key: {key}")
            return cache_data.get("value")
        except Exception as e:
            logger.warning(f"Error reading from cache: {e}")
            return None

    async def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """
        Store a value in the cache.

        Args:
            key: Cache key
            value: Value to store
            ttl: Time-to-live in seconds, or None for no expiration
        """
        cache_path = self._get_cache_path(key)

        try:
            cache_data = {
                "value": value,
                "timestamp": time.time(),
            }

            # Add expiration if TTL is provided
            if ttl is not None:
                cache_data["expiration"] = time.time() + ttl

            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)

            logger.debug(f"Cached value for key: {key}")
        except Exception as e:
            logger.warning(f"Error writing to cache: {e}")

    async def delete(self, key: str) -> bool:
        """
        Delete a value from the cache.

        Args:
            key: Cache key

        Returns:
            True if the value was deleted, False otherwise
        """
        cache_path = self._get_cache_path(key)

        if not cache_path.exists():
            return False

        try:
            cache_path.unlink()
            logger.debug(f"Deleted cache for key: {key}")
            return True
        except Exception as e:
            logger.warning(f"Error deleting from cache: {e}")
            return False

    async def clear(self, older_than: int | None = None) -> int:
        """
        Clear all cache entries or entries older than a specified time.

        Args:
            older_than: Clear only entries older than this many seconds, or None for all

        Returns:
            Number of cache entries cleared
        """
        count = 0

        try:
            for cache_file in self.cache_dir.glob("*.json"):
                try:
                    # If older_than is specified, check the file's modification time
                    if older_than is not None:
                        mtime = cache_file.stat().st_mtime
                        if time.time() - mtime < older_than:
                            continue

                    cache_file.unlink()
                    count += 1
                except Exception as e:
                    logger.warning(f"Error deleting cache file {cache_file}: {e}")

            logger.info(f"Cleared {count} cache entries")
            return count
        except Exception as e:
            logger.warning(f"Error clearing cache: {e}")
            return count

    async def get_stats(self) -> dict[str, Any]:
        """
        Get statistics about the cache.

        Returns:
            Dictionary with cache statistics
        """
        try:
            # Count files and total size
            file_count = 0
            total_size = 0
            oldest_time = time.time()
            newest_time = 0

            for cache_file in self.cache_dir.glob("*.json"):
                file_count += 1
                total_size += cache_file.stat().st_size

                mtime = cache_file.stat().st_mtime
                oldest_time = min(oldest_time, mtime)
                newest_time = max(newest_time, mtime)

            # Convert bytes to human-readable format
            size_str = self._format_size(total_size)

            return {
                "file_count": file_count,
                "total_size": total_size,
                "total_size_formatted": size_str,
                "oldest_entry": None if file_count == 0 else time.ctime(oldest_time),
                "newest_entry": None if file_count == 0 else time.ctime(newest_time),
                "cache_dir": str(self.cache_dir),
            }
        except Exception as e:
            logger.warning(f"Error getting cache stats: {e}")
            return {
                "error": str(e),
                "cache_dir": str(self.cache_dir),
            }

    def _format_size(self, size_bytes: int | float) -> str:
        """Format a size in bytes to a human-readable string."""
        size_bytes_float = float(size_bytes)  # Convert to float for division
        if size_bytes < 1024:
            return f"{size_bytes} bytes"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes_float / 1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes_float / (1024 * 1024):.1f} MB"
        else:
            return f"{size_bytes_float / (1024 * 1024 * 1024):.1f} GB"
