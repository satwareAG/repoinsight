"""
File scanning package for RepoInsight.

This package provides functionality for scanning repositories and directories
to discover and filter files for documentation.
"""

from repoinsight.scanner.engine import FileTypeDetector, RepositoryScanner
from repoinsight.scanner.filters import (
    AndFilter,
    ContentFilter,
    FileFilter,
    FilterBuilder,
    LambdaFilter,
    NotFilter,
    OrFilter,
    PatternFilter,
    RegexFilter,
    SizeFilter,
)

__all__ = [
    "RepositoryScanner",
    "FileTypeDetector",
    "FileFilter",
    "AndFilter",
    "OrFilter",
    "NotFilter",
    "PatternFilter",
    "RegexFilter",
    "SizeFilter",
    "ContentFilter",
    "LambdaFilter",
    "FilterBuilder",
]
