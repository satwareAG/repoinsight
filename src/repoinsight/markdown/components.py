"""
Markdown component generation for RepoInsight.

This module provides building blocks for generating various components
of the Markdown documentation.
"""

from pathlib import Path
from typing import Optional, Union

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, get_lexer_for_filename
from pygments.util import ClassNotFound

from repoinsight.scanner.engine import FileTypeDetector


class MarkdownComponents:
    """
    Collection of components for building Markdown documentation.
    """

    @staticmethod
    def header(title: str, level: int = 1) -> str:
        """
        Generate a Markdown header.

        Args:
            title: Header title
            level: Header level (1-6)

        Returns:
            Markdown header
        """
        # Ensure level is between 1 and 6
        level = max(1, min(6, level))
        return f"{'#' * level} {title}\n\n"

    @staticmethod
    def paragraph(text: str) -> str:
        """
        Generate a Markdown paragraph.

        Args:
            text: Paragraph text

        Returns:
            Markdown paragraph
        """
        return f"{text}\n\n"

    @staticmethod
    def code_block(code: str, language: str = "") -> str:
        """
        Generate a Markdown code block with syntax highlighting.

        Args:
            code: Source code
            language: Programming language for syntax highlighting

        Returns:
            Markdown code block
        """
        return f"```{language}\n{code}\n```\n\n"

    @staticmethod
    def list_item(text: str, level: int = 0) -> str:
        """
        Generate a Markdown list item.

        Args:
            text: Item text
            level: Indentation level

        Returns:
            Markdown list item
        """
        indent = "  " * level
        return f"{indent}- {text}\n"

    @staticmethod
    def ordered_list_item(text: str, number: int, level: int = 0) -> str:
        """
        Generate a Markdown ordered list item.

        Args:
            text: Item text
            number: Item number
            level: Indentation level

        Returns:
            Markdown ordered list item
        """
        indent = "  " * level
        return f"{indent}{number}. {text}\n"

    @staticmethod
    def table_row(cells: list[str], is_header: bool = False) -> str:
        """
        Generate a Markdown table row.

        Args:
            cells: Cell values
            is_header: Whether this is a header row

        Returns:
            Markdown table row
        """
        row = "| " + " | ".join(cells) + " |\n"

        if is_header:
            separator = "| " + " | ".join(["---"] * len(cells)) + " |\n"
            return row + separator

        return row

    @staticmethod
    def link(text: str, url: str) -> str:
        """
        Generate a Markdown link.

        Args:
            text: Link text
            url: Link URL

        Returns:
            Markdown link
        """
        return f"[{text}]({url})"

    @staticmethod
    def image(alt_text: str, url: str) -> str:
        """
        Generate a Markdown image.

        Args:
            alt_text: Image alt text
            url: Image URL

        Returns:
            Markdown image
        """
        return f"![{alt_text}]({url})"

    @staticmethod
    def horizontal_rule() -> str:
        """
        Generate a Markdown horizontal rule.

        Returns:
            Markdown horizontal rule
        """
        return "---\n\n"

    @staticmethod
    def blockquote(text: str) -> str:
        """
        Generate a Markdown blockquote.

        Args:
            text: Blockquote text

        Returns:
            Markdown blockquote
        """
        # Add blockquote prefix to each line
        lines = text.split("\n")
        quoted_lines = [f"> {line}" for line in lines]
        return "\n".join(quoted_lines) + "\n\n"

    @staticmethod
    def metadata_table(metadata: dict[str, str]) -> str:
        """
        Generate a Markdown table for file metadata.

        Args:
            metadata: Dictionary of metadata key-value pairs

        Returns:
            Markdown table
        """
        if not metadata:
            return ""

        table = "| Property | Value |\n| --- | --- |\n"
        for key, value in metadata.items():
            table += f"| **{key}** | {value} |\n"

        return table + "\n"

    @staticmethod
    def toc_entry(title: str, link: str, level: int = 0) -> str:
        """
        Generate a table of contents entry.

        Args:
            title: Entry title
            link: Entry link
            level: Indentation level

        Returns:
            Table of contents entry
        """
        indent = "  " * level
        return f"{indent}- [{title}]({link})\n"

    @staticmethod
    def toc_title() -> str:
        """
        Generate a table of contents title.

        Returns:
            Table of contents title
        """
        return "## Table of Contents\n\n"

    @staticmethod
    def file_header(
        file_path: Union[str, Path], relative_to: Optional[Union[str, Path]] = None
    ) -> str:
        """
        Generate a file header with path and language.

        Args:
            file_path: Path to the file
            relative_to: Path to make file_path relative to

        Returns:
            File header
        """
        path = Path(file_path)

        # Make path relative if requested
        if relative_to:
            try:
                path = path.relative_to(relative_to)
            except ValueError:
                # If path is not relative to relative_to, use absolute path
                pass

        # Get file language
        language = FileTypeDetector.detect_language(path)

        # Create header
        header = f"## File: {path}\n\n"
        header += f"**Language**: {language}\n\n"

        return header

    @staticmethod
    def file_content(
        file_path: Union[str, Path], content: str, syntax_highlighting: bool = True
    ) -> str:
        """
        Generate a Markdown code block for file content with proper syntax highlighting.

        Args:
            file_path: Path to the file
            content: File content
            syntax_highlighting: Whether to use syntax highlighting

        Returns:
            Markdown code block
        """
        path = Path(file_path)

        if syntax_highlighting:
            # Try to get the language from the file extension
            language = FileTypeDetector.detect_language(path)
            return MarkdownComponents.code_block(content, language)
        else:
            # Use a plain code block without syntax highlighting
            return MarkdownComponents.code_block(content)

    @staticmethod
    def file_description(description: str) -> str:
        """
        Generate a formatted file description section.

        Args:
            description: File description

        Returns:
            Formatted description
        """
        if not description:
            return ""

        return f"### Description\n\n{description}\n\n"

    @staticmethod
    def file_metadata(metadata: dict[str, str]) -> str:
        """
        Generate a formatted file metadata section.

        Args:
            metadata: File metadata

        Returns:
            Formatted metadata
        """
        if not metadata:
            return ""

        return f"### Metadata\n\n{MarkdownComponents.metadata_table(metadata)}\n\n"

    @staticmethod
    def html_syntax_highlighting(
        code: str,
        language: str,
        line_numbers: bool = False,
        style: str = "default",
    ) -> str:
        """
        Generate HTML for syntax-highlighted code.

        Args:
            code: Source code
            language: Programming language
            line_numbers: Whether to show line numbers
            style: Pygments style

        Returns:
            HTML with syntax highlighting
        """
        try:
            lexer = get_lexer_by_name(language, stripall=True)
        except ClassNotFound:
            try:
                # Try to guess the lexer
                lexer = get_lexer_for_filename(f"file.{language}", stripall=True)
            except ClassNotFound:
                # Fallback to plain text
                lexer = get_lexer_by_name("text", stripall=True)

        formatter = HtmlFormatter(
            linenos="table" if line_numbers else False,
            style=style,
            cssclass="highlight",
            full=False,
        )

        return highlight(code, lexer, formatter)

    @staticmethod
    def html_style_for_syntax_highlighting(style: str = "default") -> str:
        """
        Generate CSS for syntax highlighting.

        Args:
            style: Pygments style

        Returns:
            CSS for syntax highlighting
        """
        formatter = HtmlFormatter(style=style)
        return f"<style>\n{formatter.get_style_defs('.highlight')}\n</style>\n\n"
