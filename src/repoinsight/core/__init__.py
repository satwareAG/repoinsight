"""
Core processing package for RepoInsight.

This package provides the main processing engine that orchestrates
the entire workflow of the application.
"""

from repoinsight.core.engine import ProcessingEngine
from repoinsight.core.models import FileData, RepositorySnapshot

__all__ = [
    "ProcessingEngine",
    "FileData",
    "RepositorySnapshot",
]
