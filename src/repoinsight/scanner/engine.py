"""
File scanning engine for RepoInsight.

This module provides functionality for scanning repositories and directories
to discover files for documentation.
"""

import asyncio
import fnmatch
import os
from pathlib import Path

from repoinsight.config.models import FilePatterns


class RepositoryScanner:
    """
    Scanner for discovering and filtering files in a repository.
    """

    def __init__(
        self,
        root_path: str | Path,
        file_patterns: FilePatterns | None = None,
        exclude_dirs: list[str] | None = None,
        scan_dirs: list[str] | None = None,
    ) -> None:
        """
        Initialize a repository scanner.

        Args:
            root_path: Root path of the repository to scan
            file_patterns: Patterns for including/excluding files
            exclude_dirs: Directories to exclude from scanning
            scan_dirs: Directories to scan (relative to root_path)
        """
        self.root_path = Path(root_path)
        self.file_patterns = file_patterns or FilePatterns()
        self.exclude_dirs = set(exclude_dirs or ["venv", "node_modules", ".git"])
        self.scan_dirs = scan_dirs or ["."]

    def is_excluded_dir(self, dir_path: Path) -> bool:
        """
        Check if a directory should be excluded from scanning.

        Args:
            dir_path: Path to the directory

        Returns:
            True if the directory should be excluded, False otherwise
        """
        # Convert to relative path if it's absolute
        if dir_path.is_absolute():
            try:
                # Get relative path from root
                rel_path = dir_path.relative_to(self.root_path)
                dir_path = rel_path
            except ValueError:
                # Path is not relative to root, shouldn't happen
                return True

        dir_str = str(dir_path)

        # Check if any part of the path matches an excluded directory
        path_parts = dir_path.parts
        for part in path_parts:
            if part in self.exclude_dirs:
                return True

        # Check patterns
        return any(fnmatch.fnmatch(dir_str, pattern) for pattern in self.exclude_dirs)

    def is_included_file(self, file_path: Path) -> bool:
        """
        Check if a file should be included based on patterns.

        Args:
            file_path: Path to the file

        Returns:
            True if the file should be included, False otherwise
        """
        # Convert to relative path if it's absolute
        if file_path.is_absolute():
            try:
                # Get relative path from root
                rel_path = file_path.relative_to(self.root_path)
                file_path = rel_path
            except ValueError:
                # Path is not relative to root, shouldn't happen
                return False

        file_str = str(file_path)

        # First check exclusion patterns
        for pattern in self.file_patterns.exclude:
            if fnmatch.fnmatch(file_str, pattern):
                return False

        # Then check inclusion patterns
        return any(fnmatch.fnmatch(file_str, pattern) for pattern in self.file_patterns.include)

    def scan(self) -> list[Path]:
        """
        Scan the repository for files.

        Returns:
            List of file paths that match the inclusion/exclusion patterns
        """
        included_files = []

        for scan_dir in self.scan_dirs:
            scan_path = self.root_path / scan_dir
            if not scan_path.exists():
                continue

            # Walk the directory tree
            for root, dirs, files in os.walk(scan_path):
                root_path = Path(root)

                # Filter out excluded directories (modify dirs in-place to avoid walking them)
                dirs[:] = [d for d in dirs if not self.is_excluded_dir(root_path / d)]

                # Filter and add files
                for file in files:
                    file_path = root_path / file
                    if self.is_included_file(file_path):
                        included_files.append(file_path)

        return included_files

    async def scan_async(self) -> list[Path]:
        """
        Scan the repository asynchronously.

        This method is a coroutine wrapper around the synchronous scan method,
        but runs the scan in a separate thread to avoid blocking the event loop.

        Returns:
            List of file paths that match the inclusion/exclusion patterns
        """
        # Run the synchronous scan in a separate thread
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self.scan)


class FileTypeDetector:
    """
    Detector for file types and languages.
    """

    # Mapping of file extensions to languages
    EXTENSION_TO_LANGUAGE = {
        # Common programming languages
        "py": "python",
        "js": "javascript",
        "jsx": "javascript",
        "ts": "typescript",
        "tsx": "typescript",
        "html": "html",
        "css": "css",
        "scss": "scss",
        "less": "less",
        "json": "json",
        "md": "markdown",
        "markdown": "markdown",
        "xml": "xml",
        "yaml": "yaml",
        "yml": "yaml",
        "toml": "toml",
        "ini": "ini",
        "cfg": "ini",
        "conf": "ini",
        "sh": "bash",
        "bash": "bash",
        "bat": "batch",
        "cmd": "batch",
        "ps1": "powershell",
        "java": "java",
        "c": "c",
        "h": "c",
        "cpp": "cpp",
        "hpp": "cpp",
        "cc": "cpp",
        "hh": "cpp",
        "cs": "csharp",
        "rb": "ruby",
        "php": "php",
        "go": "go",
        "rs": "rust",
        "swift": "swift",
        "kt": "kotlin",
        "scala": "scala",
        "dart": "dart",
        "sql": "sql",
        "r": "r",
        "pl": "perl",
        "pm": "perl",
        "lua": "lua",
        "ex": "elixir",
        "exs": "elixir",
        "hs": "haskell",
        "fs": "fsharp",
        "fsx": "fsharp",
        "clj": "clojure",
        "cljs": "clojure",
        "groovy": "groovy",
        "jl": "julia",
        "m": "matlab",
        "mm": "objectivec",
        "coffee": "coffeescript",
        "elm": "elm",
        "erl": "erlang",
        "vue": "vue",
        "svelte": "svelte",
        # Document formats
        "txt": "text",
        "rst": "restructuredtext",
        "pdf": "pdf",
        "doc": "word",
        "docx": "word",
        "xls": "excel",
        "xlsx": "excel",
        "ppt": "powerpoint",
        "pptx": "powerpoint",
        # Configuration formats
        "dockerfile": "dockerfile",
        "jenkinsfile": "jenkinsfile",
        "makefile": "makefile",
        # Other formats
        "svg": "svg",
        "graphql": "graphql",
        "proto": "protobuf",
    }

    @classmethod
    def detect_language(cls, file_path: str | Path) -> str:
        """
        Detect the programming language of a file.

        Args:
            file_path: Path to the file

        Returns:
            Language identifier string, or "unknown" if the language cannot be determined
        """
        path = Path(file_path)

        # Get the file extension (lowercase, without the dot)
        extension = path.suffix.lower().lstrip(".")

        # Special case for files without extension
        if not extension:
            # Check if the filename itself is a known language identifier
            filename = path.name.lower()
            if filename in cls.EXTENSION_TO_LANGUAGE:
                return cls.EXTENSION_TO_LANGUAGE[filename]

            # Some special cases
            if filename == "dockerfile":
                return "dockerfile"
            elif filename == "makefile":
                return "makefile"
            elif filename == "jenkinsfile":
                return "jenkinsfile"

            return "text"  # Default to plain text

        # Look up the language by extension
        return cls.EXTENSION_TO_LANGUAGE.get(extension, "unknown")
