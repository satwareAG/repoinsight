"""
Git repository interaction for RepoInsight.

This module provides functionality for interacting with Git repositories,
extracting metadata, and analyzing commits.
"""

import datetime
from pathlib import Path
from typing import Union

import git
from git import Repo


class GitRepository:
    """
    Wrapper class for Git repository operations.
    """

    def __init__(self, repo_path: Union[str, Path]):
        """
        Initialize a Git repository wrapper.

        Args:
            repo_path: Path to the Git repository
        """
        self.repo_path = Path(repo_path)
        self._repo = None

    @property
    def repo(self) -> Repo:
        """Get the GitPython Repo instance, initializing it if needed."""
        if self._repo is None:
            self._repo = self._initialize_repo()
        return self._repo

    def _initialize_repo(self) -> Repo:
        """Initialize and return the GitPython Repo instance."""
        try:
            return Repo(self.repo_path)
        except git.InvalidGitRepositoryError:
            # Not a Git repository, but we'll still provide some basic functionality
            return None

    def is_git_repository(self) -> bool:
        """Check if the path is a valid Git repository."""
        try:
            self.repo  # This will initialize if needed
            return self._repo is not None
        except (git.InvalidGitRepositoryError, git.NoSuchPathError):
            return False

    async def get_metadata(self) -> dict:
        """
        Get repository metadata.

        Returns:
            Dictionary containing repository metadata
        """
        metadata = {
            "path": str(self.repo_path),
            "is_git_repository": self.is_git_repository(),
            "timestamp": datetime.datetime.now().isoformat(),
        }

        # Add Git-specific metadata if available
        if self.is_git_repository():
            try:
                metadata.update(
                    {
                        "active_branch": self.get_active_branch(),
                        "commit_hash": self.get_head_commit_hash(),
                        "commit_message": self.get_head_commit_message(),
                        "commit_date": self.get_head_commit_date(),
                        "author": self.get_head_commit_author(),
                        "remote_urls": self.get_remote_urls(),
                    }
                )
            except Exception as e:
                # Don't fail if some Git operations don't work
                metadata["git_error"] = str(e)

        return metadata

    def get_active_branch(self) -> str:
        """Get the active branch name."""
        if not self.is_git_repository():
            return "N/A"

        try:
            return self.repo.active_branch.name
        except (TypeError, ValueError):
            # This can happen in detached HEAD state
            return "HEAD detached"

    def get_head_commit_hash(self) -> str:
        """Get the HEAD commit hash."""
        if not self.is_git_repository():
            return "N/A"

        return self.repo.head.commit.hexsha

    def get_head_commit_message(self) -> str:
        """Get the HEAD commit message."""
        if not self.is_git_repository():
            return "N/A"

        return self.repo.head.commit.message.strip()

    def get_head_commit_date(self) -> str:
        """Get the HEAD commit date as ISO format string."""
        if not self.is_git_repository():
            return "N/A"

        timestamp = self.repo.head.commit.committed_date
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.isoformat()

    def get_head_commit_author(self) -> str:
        """Get the HEAD commit author."""
        if not self.is_git_repository():
            return "N/A"

        return f"{self.repo.head.commit.author.name} <{self.repo.head.commit.author.email}>"

    def get_remote_urls(self) -> list[str]:
        """Get a list of remote repository URLs."""
        if not self.is_git_repository():
            return []

        return [remote.url for remote in self.repo.remotes]

    def get_file_history(self, file_path: Union[str, Path]) -> list[dict]:
        """
        Get the commit history for a specific file.

        Args:
            file_path: Path to the file, relative to repository root

        Returns:
            List of dictionaries containing commit information
        """
        if not self.is_git_repository():
            return []

        rel_path = Path(file_path).relative_to(self.repo_path)
        str_path = str(rel_path)

        try:
            # Get commits that modified the file
            commits = list(self.repo.iter_commits(paths=str_path))

            # Format the commit information
            history = []
            for commit in commits:
                history.append(
                    {
                        "hash": commit.hexsha,
                        "short_hash": commit.hexsha[:7],
                        "message": commit.message.strip(),
                        "author": f"{commit.author.name} <{commit.author.email}>",
                        "date": datetime.datetime.fromtimestamp(commit.committed_date).isoformat(),
                    }
                )

            return history
        except Exception:
            # Return empty list if file history cannot be determined
            return []

    def get_file_blame(self, file_path: Union[str, Path]) -> list[dict]:
        """
        Get blame information for a specific file.

        Args:
            file_path: Path to the file, relative to repository root

        Returns:
            List of dictionaries containing blame information per line
        """
        if not self.is_git_repository():
            return []

        rel_path = Path(file_path).relative_to(self.repo_path)
        str_path = str(rel_path)

        try:
            # Get blame information
            blame = self.repo.git.blame(str_path, "--line-porcelain").split("\n")

            # Parse the blame output
            result: list[dict] = []
            current_commit = None
            current_line = None

            for line in blame:
                if line.startswith("^"):
                    pass  # Boundary commit
                elif line.startswith("\t"):
                    # This is the actual line content
                    if current_commit and current_line:
                        current_commit["content"] = line[1:]  # Remove tab
                        result.append(current_commit)
                        current_commit = None
                        current_line = None
                elif line.startswith("author "):
                    if current_commit:
                        current_commit["author"] = line[7:]
                elif line.startswith("author-time "):
                    if current_commit:
                        timestamp = int(line[12:])
                        dt = datetime.datetime.fromtimestamp(timestamp)
                        current_commit["date"] = dt.isoformat()
                elif line.startswith("summary "):
                    if current_commit:
                        current_commit["summary"] = line[8:]
                elif line.startswith("filename "):
                    if current_commit:
                        current_commit["filename"] = line[9:]
                elif len(line.split()) == 4 and line.split()[0].isalnum():
                    # This should be a commit header line like:
                    # d670460b4b4aece5915caf5c68d12f560a9fe3e4 1 1 1
                    # <sha> <orig-line-no> <final-line-no> <num-lines>
                    parts = line.split()
                    if len(parts[0]) == 40:  # SHA-1 is 40 chars
                        current_commit = {
                            "hash": parts[0],
                            "line_no": parts[2],
                            "line_count": parts[3],
                        }
                        current_line = parts[2]

            return result
        except Exception:
            # Return empty list if blame cannot be determined
            return []
