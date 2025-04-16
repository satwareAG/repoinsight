"""
File filtering utilities for RepoInsight.

This module provides functionality for filtering files based on various criteria
such as patterns, file size, and content.
"""

import fnmatch
import re
from collections.abc import Callable
from pathlib import Path
from re import Pattern

from repoinsight.config.models import FilePatterns


class FileFilter:
    """
    Base class for file filters.

    Filters can be combined using boolean operators (and, or, not).
    """

    def matches(self, file_path: Path) -> bool:
        """
        Check if a file matches the filter criteria.

        Args:
            file_path: Path to the file to check

        Returns:
            True if the file matches, False otherwise
        """
        raise NotImplementedError("Subclasses must implement matches()")

    def __and__(self, other: "FileFilter") -> "AndFilter":
        """Combine with another filter using AND logic."""
        return AndFilter(self, other)

    def __or__(self, other: "FileFilter") -> "OrFilter":
        """Combine with another filter using OR logic."""
        return OrFilter(self, other)

    def __invert__(self) -> "NotFilter":
        """Negate the filter."""
        return NotFilter(self)


class AndFilter(FileFilter):
    """Filter that requires both sub-filters to match."""

    def __init__(self, filter1: FileFilter, filter2: FileFilter) -> None:
        self.filter1 = filter1
        self.filter2 = filter2

    def matches(self, file_path: Path) -> bool:
        return self.filter1.matches(file_path) and self.filter2.matches(file_path)


class OrFilter(FileFilter):
    """Filter that requires at least one sub-filter to match."""

    def __init__(self, filter1: FileFilter, filter2: FileFilter) -> None:
        self.filter1 = filter1
        self.filter2 = filter2

    def matches(self, file_path: Path) -> bool:
        return self.filter1.matches(file_path) or self.filter2.matches(file_path)


class NotFilter(FileFilter):
    """Filter that negates another filter."""

    def __init__(self, base_filter: FileFilter) -> None:
        self.base_filter = base_filter

    def matches(self, file_path: Path) -> bool:
        return not self.base_filter.matches(file_path)


class PatternFilter(FileFilter):
    """Filter that matches files based on glob patterns."""

    def __init__(self, patterns: FilePatterns) -> None:
        self.patterns = patterns

    def matches(self, file_path: Path) -> bool:
        file_str = str(file_path)

        # Check exclusion patterns first
        for pattern in self.patterns.exclude:
            if fnmatch.fnmatch(file_str, pattern):
                return False

        # Then check inclusion patterns
        return any(fnmatch.fnmatch(file_str, pattern) for pattern in self.patterns.include)


class RegexFilter(FileFilter):
    """Filter that matches files based on regular expressions."""

    def __init__(
        self,
        include_patterns: list[str | Pattern] | None = None,
        exclude_patterns: list[str | Pattern] | None = None,
    ) -> None:
        self.include_patterns = []
        self.exclude_patterns = []

        # Compile include patterns
        if include_patterns:
            for pattern in include_patterns:
                if isinstance(pattern, str):
                    self.include_patterns.append(re.compile(pattern))
                else:
                    self.include_patterns.append(pattern)

        # Compile exclude patterns
        if exclude_patterns:
            for pattern in exclude_patterns:
                if isinstance(pattern, str):
                    self.exclude_patterns.append(re.compile(pattern))
                else:
                    self.exclude_patterns.append(pattern)

    def matches(self, file_path: Path) -> bool:
        file_str = str(file_path)

        # Check exclusion patterns first
        for pattern in self.exclude_patterns:
            if pattern.search(file_str):
                return False

        # If no include patterns, include everything not excluded
        if not self.include_patterns:
            return True

        # Check inclusion patterns
        return any(pattern.search(file_str) for pattern in self.include_patterns)


class SizeFilter(FileFilter):
    """Filter that matches files based on size."""

    def __init__(self, min_size: int | None = None, max_size: int | None = None) -> None:
        """
        Initialize a size filter.

        Args:
            min_size: Minimum file size in bytes (inclusive), or None for no minimum
            max_size: Maximum file size in bytes (inclusive), or None for no maximum
        """
        self.min_size = min_size
        self.max_size = max_size

    def matches(self, file_path: Path) -> bool:
        if not file_path.is_file():
            return False

        size = file_path.stat().st_size

        if self.min_size is not None and size < self.min_size:
            return False

        if self.max_size is not None and size > self.max_size:
            return False

        return True


class ContentFilter(FileFilter):
    """Filter that matches files based on their content."""

    def __init__(
        self,
        pattern: str | Pattern | Callable[[str], bool],
        max_size: int | None = 1024 * 1024,  # Default: 1MB
        encoding: str = "utf-8",
    ) -> None:
        """
        Initialize a content filter.

        Args:
            pattern: String pattern, compiled regex, or callback function to match content
            max_size: Maximum file size to read, or None for no limit
            encoding: File encoding to use when reading
        """
        self.max_size = max_size
        self.encoding = encoding
        
        # Properly type the matcher function
        self.matcher: Callable[[str], bool]
        
        if isinstance(pattern, str):
            regex = re.compile(pattern)
            self.matcher = lambda text: bool(regex.search(text))
        elif hasattr(pattern, "search"):
            # Create a wrapper function to handle the overloaded method
            self.matcher = lambda text: bool(pattern.search(text))
        else:
            self.matcher = pattern

    def matches(self, file_path: Path) -> bool:
        if not file_path.is_file():
            return False

        # Check file size if max_size is set
        if self.max_size is not None:
            size = file_path.stat().st_size
            if size > self.max_size:
                return False

        try:
            # Read the file content
            with open(file_path, encoding=self.encoding) as f:
                content = f.read()

            # Match the content
            return bool(self.matcher(content))
        except (OSError, UnicodeDecodeError):
            # If we can't read the file, assume it doesn't match
            return False


class FilterBuilder:
    """Utility for building complex file filters."""

    @staticmethod
    def from_patterns(patterns: FilePatterns) -> FileFilter:
        """Create a filter from FilePatterns."""
        return PatternFilter(patterns)

    @staticmethod
    def from_config(config) -> FileFilter:
        """Create a filter from RepoInsightConfig."""
        # Create the base pattern filter
        pattern_filter = PatternFilter(config.file_patterns)

        # Create filters for excluded directories
        excluded_dirs = config.exclude_directories

        def directory_filter(path: Path) -> bool:
            # Check if any part of the path is in excluded_dirs
            path_parts = path.parts
            return not any(part in excluded_dirs for part in path_parts)

        # Combine pattern filter with directory exclusion
        return AndFilter(pattern_filter, LambdaFilter(directory_filter))

    @staticmethod
    def binary_filter() -> FileFilter:
        """Create a filter that excludes binary files."""
        return NotFilter(ContentFilter(lambda content: b"\0" in content[:1024].encode()))

    @staticmethod
    def size_filter(max_size: int) -> FileFilter:
        """Create a filter that excludes files larger than max_size."""
        return SizeFilter(max_size=max_size)


class LambdaFilter(FileFilter):
    """Filter that uses a custom function to determine matches."""

    def __init__(self, func: Callable[[Path], bool]) -> None:
        """
        Initialize a lambda filter.

        Args:
            func: Function that takes a Path and returns True if it matches
        """
        self.func = func

    def matches(self, file_path: Path) -> bool:
        return self.func(file_path)
