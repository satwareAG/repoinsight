"""
Git integration package for RepoInsight.

This package provides functionality for interacting with Git repositories
and extracting metadata for documentation.
"""

from repoinsight.git.metadata import GitMetadataExtractor
from repoinsight.git.repository import GitRepository

__all__ = ["GitRepository", "GitMetadataExtractor"]
