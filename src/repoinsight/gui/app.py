"""
Main GUI application module for RepoInsight.

This module provides the main application entry point for the GUI.
"""

import logging
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMessageBox

from repoinsight import __version__
from repoinsight.config.models import RepoInsightConfig
from repoinsight.gui.config_panel import ConfigPanel
from repoinsight.gui.main_window import MainWindow
from repoinsight.gui.preview_panel import MarkdownPreviewPanel
from repoinsight.gui.profile_panel import ProfilePanel
from repoinsight.gui.worker import DocumentationWorker

# Set up logging
logger = logging.getLogger(__name__)


def run_app() -> int:
    """
    Run the RepoInsight GUI application.

    Returns:
        Exit code
    """
    # Initialize application
    app = QApplication(sys.argv)
    app.setApplicationName("RepoInsight")
    app.setApplicationVersion(__version__)

    # Create main window
    main_window = MainWindow()
    # Add worker attribute to store reference
    main_window._worker = None

    # Create and set up profile panel
    profile_panel = ProfilePanel(main_window.config_manager)
    main_window.left_layout.insertWidget(0, profile_panel)

    # Create and set up config panel
    config_panel = ConfigPanel()
    main_window.center_layout.insertWidget(0, config_panel)

    # Create and set up preview panel
    preview_panel = MarkdownPreviewPanel()
    main_window.right_layout.insertWidget(0, preview_panel)

    # Add worker management to main window
    def _on_profile_selected(config: "RepoInsightConfig") -> None:
        """Handle profile selection."""
        main_window.current_config = config

    def _on_config_changed(config: "RepoInsightConfig") -> None:
        """Handle configuration changes."""
        main_window.current_config = config
        # In a real implementation, we might want to update the UI based on the new config

    def _on_repository_opened(repo_path: Path) -> None:
        """Handle repository opening."""
        # In a real implementation, we might want to scan the repository
        # and update the UI based on the results
        main_window.status_label.setText(f"Repository: {repo_path}")

    def _on_generation_started() -> None:
        """Handle generation start."""
        if not main_window.current_config:
            QMessageBox.warning(
                main_window,
                "Configuration Error",
                "No configuration available. Please open a repository first.",
            )
            return

        # Stop any existing worker
        if main_window._worker and main_window._worker.is_running():
            main_window._worker.stop()

        # Initialize worker and store reference in main_window
        main_window._worker = DocumentationWorker(main_window.current_config)

        # Connect worker signals
        main_window._worker.started.connect(
            lambda: main_window.status_label.setText("Documentation generation started...")
        )
        main_window._worker.progress.connect(lambda p, m: main_window._update_progress(p, m))
        main_window._worker.finished.connect(lambda markdown: main_window._on_generation_completed(markdown))
        main_window._worker.error.connect(lambda msg: main_window._on_generation_error(msg))

        # Start worker
        main_window._worker.start()

    def _update_progress(percentage: int, message: str) -> None:
        """Update progress bar and status message."""
        main_window.progress_bar.setValue(percentage)
        main_window.progress_bar.setVisible(True)
        main_window.status_label.setText(message)

    def _on_generation_completed(markdown: str) -> None:
        """Handle generation completion."""
        main_window.progress_bar.setVisible(False)
        main_window.status_label.setText("Documentation generation completed")

        if markdown:
            # Emit signal with the generated markdown
            main_window.generation_completed.emit(markdown)
        else:
            QMessageBox.warning(
                main_window,
                "Generation Error",
                "Failed to generate documentation. Please check the logs for details.",
            )

    def _on_generation_error(message: str) -> None:
        """Handle generation error."""
        main_window.progress_bar.setVisible(False)
        main_window.status_label.setText(f"Error: {message}")

        QMessageBox.critical(
            main_window,
            "Generation Error",
            f"An error occurred during documentation generation:\n\n{message}",
        )

    # Attach methods to main window
    main_window._on_profile_selected = _on_profile_selected
    main_window._on_config_changed = _on_config_changed
    main_window._on_repository_opened = _on_repository_opened
    main_window._on_generation_started = _on_generation_started
    main_window._update_progress = _update_progress
    main_window._on_generation_completed = _on_generation_completed
    main_window._on_generation_error = _on_generation_error

    # Connect signals and slots after attaching methods

    # Connect profile panel signals
    profile_panel.profile_selected.connect(config_panel.set_config)
    profile_panel.profile_selected.connect(main_window._on_profile_selected)

    # Connect config panel signals
    config_panel.config_changed.connect(main_window._on_config_changed)

    # Connect main window signals
    main_window.config_changed.connect(config_panel.set_config)
    main_window.repository_opened.connect(main_window._on_repository_opened)
    main_window.generation_started.connect(main_window._on_generation_started)
    main_window.generation_completed.connect(preview_panel.set_markdown)

    # Run the application
    main_window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(run_app())
