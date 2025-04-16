"""
Git metadata extraction for RepoInsight.

This module handles the extraction and formatting of Git metadata for documentation.
"""

import datetime
from pathlib import Path
from typing import Union

from repoinsight.git.repository import GitRepository


class GitMetadataExtractor:
    """
    Extracts formatted metadata from Git repositories for documentation.
    """

    def __init__(self, repository: GitRepository):
        """
        Initialize a Git metadata extractor.

        Args:
            repository: GitRepository instance to extract metadata from
        """
        self.repository = repository

    async def extract_repository_metadata(self) -> dict:
        """
        Extract comprehensive repository metadata for documentation.

        Returns:
            Dictionary containing formatted repository metadata
        """
        # Get basic metadata from the repository
        metadata = await self.repository.get_metadata()

        # Format the metadata for documentation
        formatted = {
            "Repository Information": {
                "Path": metadata["path"],
                "Git Repository": "Yes" if metadata["is_git_repository"] else "No",
                "Generated": metadata["timestamp"],
            }
        }

        # Add Git-specific information if available
        if metadata.get("is_git_repository"):
            formatted["Git Information"] = {
                "Branch": metadata.get("active_branch", "N/A"),
                "Commit": metadata.get("commit_hash", "N/A"),
                "Commit Message": metadata.get("commit_message", "N/A"),
                "Commit Date": metadata.get("commit_date", "N/A"),
                "Author": metadata.get("author", "N/A"),
            }

            if metadata.get("remote_urls"):
                formatted["Remote Repositories"] = {
                    f"Remote {i+1}": url for i, url in enumerate(metadata.get("remote_urls", []))
                }

        return formatted

    def format_as_markdown(self, metadata: dict) -> str:
        """
        Format the repository metadata as Markdown.

        Args:
            metadata: Repository metadata dictionary from extract_repository_metadata

        Returns:
            Formatted Markdown string
        """
        lines = ["# Repository Metadata\n"]

        for section, data in metadata.items():
            lines.append(f"## {section}\n")

            for key, value in data.items():
                # Handle special cases like lists
                if isinstance(value, list):
                    value_str = ", ".join(value)
                else:
                    value_str = str(value)

                lines.append(f"- **{key}:** {value_str}")

            lines.append("")  # Empty line between sections

        return "\n".join(lines)

    async def generate_file_metadata(self, file_path: Union[str, Path]) -> dict:
        """
        Generate metadata for a specific file, including Git history if available.

        Args:
            file_path: Path to the file

        Returns:
            Dictionary containing file metadata
        """
        path = Path(file_path)

        # Basic file metadata
        file_metadata = {
            "path": str(path),
            "name": path.name,
            "extension": path.suffix.lstrip(".").lower() if path.suffix else "",
            "size_bytes": path.stat().st_size if path.exists() else 0,
            "last_modified": datetime.datetime.fromtimestamp(
                path.stat().st_mtime if path.exists() else 0
            ).isoformat(),
        }

        # Add Git metadata if available
        if self.repository.is_git_repository():
            try:
                rel_path = path.relative_to(self.repository.repo_path)
                history = self.repository.get_file_history(rel_path)

                if history:
                    file_metadata["git_history"] = {
                        "last_commit": history[0],
                        "commit_count": len(history),
                        "first_commit": history[-1] if len(history) > 0 else None,
                    }
            except (ValueError, Exception):
                # File might be outside repo or other error
                pass

        return file_metadata

    def format_file_metadata_as_markdown(self, metadata: dict) -> str:
        """
        Format file metadata as Markdown.

        Args:
            metadata: File metadata dictionary from generate_file_metadata

        Returns:
            Formatted Markdown string
        """
        lines = [f"# File: {metadata['name']}\n"]

        # Basic metadata
        lines.append("## File Information\n")
        lines.append(f"- **Path:** {metadata['path']}")
        lines.append(f"- **Size:** {self._format_file_size(metadata['size_bytes'])}")
        lines.append(f"- **Last Modified:** {metadata['last_modified']}")
        if metadata.get("extension"):
            lines.append(f"- **Type:** {metadata['extension']}")
        lines.append("")

        # Git history if available
        if "git_history" in metadata:
            history = metadata["git_history"]
            lines.append("## Git History\n")

            if history.get("last_commit"):
                commit = history["last_commit"]
                lines.append("### Latest Commit\n")
                lines.append(f"- **Hash:** {commit['hash']}")
                lines.append(f"- **Date:** {commit['date']}")
                lines.append(f"- **Author:** {commit['author']}")
                lines.append(f"- **Message:** {commit['message']}")
                lines.append("")

            if history.get("commit_count"):
                lines.append(f"- **Total Commits:** {history['commit_count']}")

            if history.get("first_commit"):
                commit = history["first_commit"]
                lines.append("\n### First Commit\n")
                lines.append(f"- **Hash:** {commit['hash']}")
                lines.append(f"- **Date:** {commit['date']}")
                lines.append(f"- **Author:** {commit['author']}")
                lines.append(f"- **Message:** {commit['message']}")

            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def _format_file_size(size_bytes: int) -> str:
        """Format file size in a human-readable way."""
        if size_bytes < 1024:
            return f"{size_bytes} bytes"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"
