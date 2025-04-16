"""
Core processing engine for RepoInsight.

This module provides the main processing engine that orchestrates
the entire workflow of the application.
"""

import asyncio
import logging
import os
from pathlib import Path

from repoinsight.config.models import RepoInsightConfig
from repoinsight.core.models import FileData, RepositorySnapshot
from repoinsight.git.metadata import GitMetadataExtractor
from repoinsight.git.repository import GitRepository
from repoinsight.llm.client import LLMClient
from repoinsight.markdown.generator import MarkdownGenerator
from repoinsight.scanner.engine import FileTypeDetector, RepositoryScanner

logger = logging.getLogger(__name__)


class ProcessingEngine:
    """
    Main processing engine for RepoInsight.

    This class orchestrates the entire workflow, from scanning files
    to generating descriptions and producing the final markdown output.
    """

    def __init__(self, config: RepoInsightConfig) -> None:
        """
        Initialize the processing engine.

        Args:
            config: Configuration for the engine
        """
        self.config = config
        self.max_concurrency = min(os.cpu_count() or 4, config.processing.max_concurrent_tasks)
        self.semaphore = asyncio.Semaphore(self.max_concurrency)

        # Initialize components
        self.llm_client: LLMClient | None = None  # Properly typed to allow None or LLMClient
        self._init_components()

    def _init_components(self) -> None:
        """Initialize the various components based on configuration."""
        # Initialize Git repository
        self.repository = GitRepository(self.config.get_absolute_root_path())
        self.metadata_extractor = GitMetadataExtractor(self.repository)

        # Initialize LLM client if enabled
        if self.config.llm.enabled:
            cache_dir = (
                self.config.get_absolute_cache_path() if self.config.llm.cache_enabled else None
            )
            self.llm_client = LLMClient(
                base_url=self.config.llm.api_base_url,
                api_key=self.config.llm.api_key,
                timeout=self.config.llm.timeout,
                cache_dir=cache_dir,
            )
        else:
            self.llm_client = None

        # Initialize scanner
        self.scanner = RepositoryScanner(
            self.config.get_absolute_root_path(),
            self.config.file_patterns,
            self.config.exclude_directories,
            self.config.scan_directories,
        )

        # Initialize markdown generator
        self.markdown_generator = MarkdownGenerator(
            include_toc=self.config.output.include_toc,
            include_metadata=self.config.output.include_metadata,
            include_file_stats=self.config.output.include_file_stats,
            include_commit_info=self.config.output.include_commit_info,
            syntax_highlighting=self.config.output.syntax_highlighting,
        )

    async def process_repository(self) -> RepositorySnapshot:
        """
        Process the repository and generate a snapshot.

        Returns:
            Repository snapshot with all processed files
        """
        logger.info(f"Processing repository: {self.config.root_path}")

        # Create repository snapshot
        snapshot = RepositorySnapshot(
            name=self.config.name,
            root_path=self.config.root_path,
        )

        # Extract repository metadata
        snapshot.metadata = await self.metadata_extractor.extract_repository_metadata()

        # Scan for files
        files = await self.scanner.scan_async()
        logger.info(f"Found {len(files)} files to process")

        # Process files with controlled concurrency
        tasks = []
        for file_path in files:
            task = self._process_file_with_semaphore(file_path)
            tasks.append(task)

        file_results = await asyncio.gather(*tasks, return_exceptions=True)

        # Filter and handle exceptions
        for i, result in enumerate(file_results):
            if isinstance(result, Exception):
                logger.error(f"Error processing {files[i]}: {result}")
            else:
                snapshot.add_file(result)

        logger.info(f"Successfully processed {len(snapshot.files)} files")
        return snapshot

    async def _process_file_with_semaphore(self, file_path: Path) -> FileData:
        """
        Process a file with semaphore-controlled concurrency.

        Args:
            file_path: Path to the file

        Returns:
            Processed file data
        """
        async with self.semaphore:
            return await self._process_file(file_path)

    async def _process_file(self, file_path: Path) -> FileData:
        """
        Process a single file.

        Args:
            file_path: Path to the file

        Returns:
            Processed file data
        """
        logger.debug(f"Processing file: {file_path}")

        try:
            # Read file content
            with open(file_path, encoding="utf-8", errors="replace") as f:
                content = f.read()

            # Get file metadata
            metadata = await self.metadata_extractor.generate_file_metadata(file_path)

            # Detect language
            language = FileTypeDetector.detect_language(file_path)

            # Generate description if LLM is enabled
            description = None
            if self.llm_client and self.config.llm.enabled:
                # Get commit hash for caching if available
                commit_hash = None
                if self.repository.is_git_repository():
                    commit_hash = self.repository.get_head_commit_hash()

                # Generate description
                description = await self.llm_client.generate_description(
                    file_path=file_path,
                    file_content=content,
                    language=language,
                    model=self.config.llm.model,
                    temperature=self.config.llm.temperature,
                    max_tokens=self.config.llm.max_tokens,
                    system_prompt_template=self.config.llm.system_prompt_template,
                    commit_hash=commit_hash,
                )

            # Create and return file data
            return FileData(
                path=file_path,
                content=content,
                description=description,
                metadata=metadata,
            )
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {e}")
            raise

    async def generate_markdown(self, snapshot: RepositorySnapshot) -> str:
        """
        Generate Markdown documentation from a repository snapshot.

        Args:
            snapshot: Repository snapshot

        Returns:
            Markdown document
        """
        return self.markdown_generator.generate(snapshot.to_dict())

    async def process_and_generate(self) -> tuple[RepositorySnapshot, str]:
        """
        Process the repository and generate Markdown documentation.

        Returns:
            Tuple of repository snapshot and Markdown document
        """
        # Process repository
        snapshot = await self.process_repository()

        # Generate markdown
        markdown = await self.generate_markdown(snapshot)

        # Save output if path is specified
        if self.config.output_path:
            output_path = self.config.get_absolute_output_path()
            if output_path:
                # Ensure directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Write markdown to file
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(markdown)

                logger.info(f"Markdown saved to: {output_path}")

        return snapshot, markdown
