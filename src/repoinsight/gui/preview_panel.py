"""
Markdown preview panel for RepoInsight GUI.

This module provides a component for displaying markdown content with syntax highlighting.
"""

import logging

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

logger = logging.getLogger(__name__)


class MarkdownPreviewPanel(QWidget):
    """
    Panel for displaying markdown content with preview and raw views.

    This panel provides a tabbed interface with both a rendered markdown view
    and a plain text view of the raw markdown content.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.markdown_content = ""

        # Initialize UI
        self._init_ui()

    def _init_ui(self) -> None:
        """Initialize the UI components."""
        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)

        # Add header label
        header_label = QLabel("<b>Preview</b>")
        main_layout.addWidget(header_label)

        # Create tab widget for different views
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Create rendered view tab
        self.rendered_tab = QWidget()
        rendered_layout = QVBoxLayout(self.rendered_tab)
        rendered_layout.setContentsMargins(0, 0, 0, 0)

        # Add web view for rendered markdown
        self.web_view = QWebEngineView()
        self.web_view.setContextMenuPolicy(
            Qt.ContextMenuPolicy.NoContextMenu
        )  # Disable right-click menu
        rendered_layout.addWidget(self.web_view)

        self.tab_widget.addTab(self.rendered_tab, "Rendered")

        # Create raw view tab
        self.raw_tab = QWidget()
        raw_layout = QVBoxLayout(self.raw_tab)
        raw_layout.setContentsMargins(0, 0, 0, 0)

        # Add text edit for raw markdown
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QFont("Monospace", 10))
        raw_layout.addWidget(self.text_edit)

        self.tab_widget.addTab(self.raw_tab, "Raw")

        # Add controls
        controls_layout = QHBoxLayout()

        # Add refresh button
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self._refresh_preview)
        controls_layout.addWidget(self.refresh_button)

        # Add save button
        self.save_button = QPushButton("Save As...")
        self.save_button.clicked.connect(self._save_markdown)
        controls_layout.addWidget(self.save_button)

        controls_layout.addStretch()

        main_layout.addLayout(controls_layout)

    def set_markdown(self, content: str) -> None:
        """Set the markdown content to display."""
        if content == self.markdown_content:
            return

        self.markdown_content = content

        # Update raw view
        self.text_edit.setText(content)

        # Update rendered view
        self._update_rendered_view()

    def _update_rendered_view(self) -> None:
        """Update the rendered markdown view."""
        if not self.markdown_content:
            self.web_view.setHtml("<p>No content to display.</p>")
            return

        # Convert markdown to HTML
        # In a real implementation, we would use a proper markdown to HTML converter
        # For this example, we'll use a simple HTML template with the markdown content
        # displayed in a pre tag
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
                    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                pre {{
                    background-color: #f6f8fa;
                    border-radius: 3px;
                    padding: 16px;
                    overflow: auto;
                }}
                code {{
                    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
                    font-size: 14px;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    margin-top: 24px;
                    margin-bottom: 16px;
                    font-weight: 600;
                    line-height: 1.25;
                }}
                h1 {{
                    padding-bottom: 0.3em;
                    font-size: 2em;
                    border-bottom: 1px solid #eaecef;
                }}
                h2 {{
                    padding-bottom: 0.3em;
                    font-size: 1.5em;
                    border-bottom: 1px solid #eaecef;
                }}
                h3 {{
                    font-size: 1.25em;
                }}
                a {{
                    color: #0366d6;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                blockquote {{
                    padding: 0 1em;
                    color: #6a737d;
                    border-left: 0.25em solid #dfe2e5;
                    margin: 0;
                }}
                table {{
                    border-spacing: 0;
                    border-collapse: collapse;
                    margin-bottom: 16px;
                }}
                table th, table td {{
                    padding: 6px 13px;
                    border: 1px solid #dfe2e5;
                }}
                table tr:nth-child(2n) {{
                    background-color: #f6f8fa;
                }}
            </style>
        </head>
        <body>
            <div id="content">
                <pre><code>{self.markdown_content}</code></pre>
            </div>
        </body>
        </html>
        """  # noqa: E501

        self.web_view.setHtml(html_content)

    def _refresh_preview(self) -> None:
        """Refresh the preview."""
        self._update_rendered_view()

    def _save_markdown(self) -> None:
        """Save the markdown content to a file."""
        # In a real implementation, we would show a file dialog
        # and save the content to the selected file


class MarkdownHighlighter:
    """
    Utility class for adding syntax highlighting to markdown text.

    This class would use the QSyntaxHighlighter class to add
    syntax highlighting to the raw markdown view. It is not
    implemented in this example.
    """
