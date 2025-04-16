"""
Data models for the RepoInsight core processing engine.

This module defines the data structures used to represent files, repositories,
and other entities in the processing pipeline.
"""

import datetime
from pathlib import Path


class FileData:
    """
    Data structure representing a file in the repository.
    """

    def __init__(
        self,
        path: str | Path,
        content: str | None = None,
        description: str | None = None,
        metadata: dict | None = None,
    ) -> None:
        """
        Initialize file data.

        Args:
            path: Path to the file
            content: File content
            description: Generated description
            metadata: File metadata
        """
        self.path = str(path)
        self.content = content
        self.description = description
        self.metadata = metadata or {}

    def to_dict(self) -> dict:
        """
        Convert to a dictionary representation.

        Returns:
            Dictionary representation
        """
        return {
            "path": self.path,
            "content": self.content,
            "description": self.description,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "FileData":
        """
        Create a FileData instance from a dictionary.

        Args:
            data: Dictionary representation

        Returns:
            FileData instance
        """
        return cls(
            path=data["path"],
            content=data.get("content"),
            description=data.get("description"),
            metadata=data.get("metadata"),
        )


class RepositorySnapshot:
    """
    Data structure representing a snapshot of a repository.
    """

    def __init__(
        self,
        name: str,
        root_path: str | Path,
        files: list[FileData] | None = None,
        metadata: dict | None = None,
        generation_timestamp: str | None = None,
    ) -> None:
        """
        Initialize repository snapshot.

        Args:
            name: Repository name
            root_path: Repository root path
            files: List of files
            metadata: Repository metadata
            generation_timestamp: When the snapshot was generated
        """
        self.name = name
        self.root_path = str(root_path)
        self.files = files or []
        self.metadata = metadata or {}

        # Use provided timestamp or generate a new one
        if generation_timestamp:
            self.generation_timestamp = generation_timestamp
        else:
            self.generation_timestamp = datetime.datetime.now().isoformat()

    def add_file(self, file_data: FileData) -> None:
        """
        Add a file to the repository snapshot.

        Args:
            file_data: File data to add
        """
        self.files.append(file_data)

    def to_dict(self) -> dict:
        """
        Convert to a dictionary representation.

        Returns:
            Dictionary representation
        """
        return {
            "name": self.name,
            "root_path": self.root_path,
            "files": [file.to_dict() for file in self.files],
            "metadata": self.metadata,
            "generation_timestamp": self.generation_timestamp,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "RepositorySnapshot":
        """
        Create a RepositorySnapshot instance from a dictionary.

        Args:
            data: Dictionary representation

        Returns:
            RepositorySnapshot instance
        """
        files = [FileData.from_dict(file_data) for file_data in data.get("files", [])]

        return cls(
            name=data["name"],
            root_path=data["root_path"],
            files=files,
            metadata=data.get("metadata"),
            generation_timestamp=data.get("generation_timestamp"),
        )

    def save_to_file(self, file_path: str | Path) -> None:
        """
        Save the repository snapshot to a JSON file.

        Args:
            file_path: Path to save the file to
        """
        import json
        from pathlib import Path

        # Convert to dictionary
        snapshot_dict = self.to_dict()

        # Ensure directory exists
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        # Write to file
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snapshot_dict, f, indent=2)

    @classmethod
    def load_from_file(cls, file_path: str | Path) -> "RepositorySnapshot":
        """
        Load a repository snapshot from a JSON file.

        Args:
            file_path: Path to the file

        Returns:
            RepositorySnapshot instance
        """
        import json

        # Read from file
        with open(file_path, encoding="utf-8") as f:
            snapshot_dict = json.load(f)

        # Create instance
        return cls.from_dict(snapshot_dict)
