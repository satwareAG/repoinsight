"""
Markdown document generation for RepoInsight.

This module provides functionality for generating complete Markdown documentation
from repository files and metadata.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from repoinsight.markdown.components import MarkdownComponents


class MarkdownGenerator:
    """
    Generator for Markdown documentation from repository files.
    """
    
    def __init__(self, 
                 include_toc: bool = True,
                 include_metadata: bool = True,
                 include_file_stats: bool = True,
                 include_commit_info: bool = True,
                 syntax_highlighting: bool = True):
        """
        Initialize a Markdown generator.
        
        Args:
            include_toc: Whether to include a table of contents
            include_metadata: Whether to include repository metadata
            include_file_stats: Whether to include file statistics
            include_commit_info: Whether to include commit information
            syntax_highlighting: Whether to use syntax highlighting
        """
        self.include_toc = include_toc
        self.include_metadata = include_metadata
        self.include_file_stats = include_file_stats
        self.include_commit_info = include_commit_info
        self.syntax_highlighting = syntax_highlighting
        
    def generate(self, repository_snapshot: Dict) -> str:
        """
        Generate a complete Markdown document for a repository snapshot.
        
        Args:
            repository_snapshot: Repository snapshot data
            
        Returns:
            Complete Markdown document
        """
        sections = []
        
        # Add title
        if "name" in repository_snapshot:
            title = f"{repository_snapshot['name']} Documentation"
        else:
            title = "Repository Documentation"
            
        sections.append(MarkdownComponents.header(title, 1))
        
        # Add metadata section
        if self.include_metadata and "metadata" in repository_snapshot:
            sections.append(self._generate_metadata_section(repository_snapshot["metadata"]))
            
        # Generate file sections and collect TOC entries
        file_sections = []
        toc_entries = []
        
        if "files" in repository_snapshot and repository_snapshot["files"]:
            # Create an ID counter for generating unique anchors
            id_counter = 0
            
            for file_data in repository_snapshot["files"]:
                # Generate a unique file ID for anchoring
                file_id = self._generate_file_id(file_data["path"], id_counter)
                id_counter += 1
                
                # Generate the file section
                file_section = self._generate_file_section(
                    file_data,
                    file_id,
                    repository_snapshot.get("root_path", ""),
                )
                
                # Add to file sections
                file_sections.append(file_section)
                
                # Add to TOC entries
                toc_entry = self._generate_toc_entry(
                    file_data["path"],
                    file_id,
                    repository_snapshot.get("root_path", ""),
                )
                toc_entries.append(toc_entry)
                
        # Add TOC if enabled and we have files
        if self.include_toc and toc_entries:
            sections.append(self._generate_toc(toc_entries))
            
        # Add all file sections
        sections.extend(file_sections)
        
        # Add generation info
        if "generation_timestamp" in repository_snapshot:
            sections.append(self._generate_generation_info(repository_snapshot))
            
        # Join all sections
        return "\n".join(sections)
        
    def _generate_metadata_section(self, metadata: Dict) -> str:
        """
        Generate the repository metadata section.
        
        Args:
            metadata: Repository metadata
            
        Returns:
            Formatted metadata section
        """
        section = MarkdownComponents.header("Repository Information", 2)
        
        # Format the metadata as a series of sections
        for section_name, section_data in metadata.items():
            if isinstance(section_data, dict):
                section += MarkdownComponents.header(section_name, 3)
                
                # Convert the section data to a list of key-value pairs
                formatted_data = {}
                for key, value in section_data.items():
                    # Format value based on its type
                    if isinstance(value, list):
                        formatted_value = ", ".join(map(str, value))
                    else:
                        formatted_value = str(value)
                        
                    formatted_data[key] = formatted_value
                    
                section += MarkdownComponents.metadata_table(formatted_data)
                
        return section
        
    def _generate_file_section(self, file_data: Dict, file_id: str, root_path: str) -> str:
        """
        Generate a section for a single file.
        
        Args:
            file_data: File data
            file_id: Unique file ID for anchoring
            root_path: Repository root path
            
        Returns:
            Formatted file section
        """
        # Extract file data
        file_path = file_data["path"]
        file_content = file_data.get("content", "")
        file_description = file_data.get("description", "")
        file_metadata = file_data.get("metadata", {})
        
        # Start with the file header
        section = f'<a id="{file_id}"></a>\n\n'  # Add anchor
        section += MarkdownComponents.file_header(file_path, root_path)
        
        # Add description if available
        if file_description:
            section += MarkdownComponents.file_description(file_description)
            
        # Add metadata if enabled and available
        if self.include_file_stats and file_metadata:
            # Format metadata for display
            formatted_metadata = {}
            
            # Basic file stats
            if "size_bytes" in file_metadata:
                formatted_metadata["Size"] = self._format_file_size(file_metadata["size_bytes"])
                
            if "last_modified" in file_metadata:
                formatted_metadata["Last Modified"] = file_metadata["last_modified"]
                
            if "extension" in file_metadata:
                formatted_metadata["Type"] = file_metadata["extension"]
                
            # Git history if available and enabled
            if self.include_commit_info and "git_history" in file_metadata:
                history = file_metadata["git_history"]
                
                if "last_commit" in history:
                    commit = history["last_commit"]
                    formatted_metadata["Last Commit"] = f"{commit['short_hash']} - {commit['message']}"
                    formatted_metadata["Author"] = commit["author"]
                    formatted_metadata["Date"] = commit["date"]
                    
                if "commit_count" in history:
                    formatted_metadata["Commit Count"] = str(history["commit_count"])
                    
            # Add metadata table
            if formatted_metadata:
                section += MarkdownComponents.file_metadata(formatted_metadata)
                
        # Add file content
        if file_content:
            section += MarkdownComponents.file_content(
                file_path,
                file_content,
                self.syntax_highlighting,
            )
            
        return section
        
    def _generate_toc(self, toc_entries: List[Dict]) -> str:
        """
        Generate a table of contents.
        
        Args:
            toc_entries: List of TOC entries
            
        Returns:
            Formatted table of contents
        """
        toc = MarkdownComponents.toc_title()
        
        # Add each TOC entry
        for entry in toc_entries:
            toc += MarkdownComponents.toc_entry(
                entry["title"],
                entry["link"],
                entry.get("level", 0),
            )
            
        return toc + "\n"
        
    def _generate_toc_entry(self, file_path: str, file_id: str, root_path: str) -> Dict:
        """
        Generate a table of contents entry for a file.
        
        Args:
            file_path: Path to the file
            file_id: Unique file ID for linking
            root_path: Repository root path
            
        Returns:
            TOC entry as a dictionary
        """
        path = Path(file_path)
        
        # Make path relative if possible
        if root_path:
            try:
                display_path = path.relative_to(root_path)
            except ValueError:
                display_path = path
        else:
            display_path = path
            
        # Create the TOC entry
        return {
            "title": str(display_path),
            "link": f"#{file_id}",
            "level": len(display_path.parts) - 1,  # Indent based on path depth
        }
        
    def _generate_file_id(self, file_path: str, counter: int) -> str:
        """
        Generate a unique ID for a file.
        
        Args:
            file_path: Path to the file
            counter: Unique counter
            
        Returns:
            Unique file ID
        """
        # Convert path to a safe string for use as an HTML ID
        safe_path = re.sub(r'[^a-zA-Z0-9-]', '_', str(file_path))
        
        # Append counter to ensure uniqueness
        return f"file_{safe_path}_{counter}"
        
    def _generate_generation_info(self, repository_snapshot: Dict) -> str:
        """
        Generate information about when the documentation was generated.
        
        Args:
            repository_snapshot: Repository snapshot data
            
        Returns:
            Formatted generation info
        """
        timestamp = repository_snapshot.get("generation_timestamp", "")
        
        if not timestamp:
            return ""
            
        return f"\n\n---\n\nGenerated at: {timestamp}\n"
        
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
