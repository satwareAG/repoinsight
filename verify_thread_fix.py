#!/usr/bin/env python
"""
Verification script for the thread handling fix in RepoInsight GUI.

This script tests the fix for the "QThread: Destroyed while thread is still running" issue
by launching the GUI, clicking the Run button, and then closing the application.
"""

import logging
import sys
import time
from functools import partial

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from repoinsight.gui.main_window import MainWindow

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def run_test():
    """Run the GUI test with automated actions."""
    # Initialize the application
    app = QApplication(sys.argv)
    app.setApplicationName("RepoInsight Test")
    
    # Import required components
    from repoinsight.config.yaml import ConfigManager
    from repoinsight.gui.config_panel import ConfigPanel
    from repoinsight.gui.preview_panel import MarkdownPreviewPanel
    from repoinsight.gui.profile_panel import ProfilePanel
    from repoinsight import __version__
    
    # Create main window
    main_window = MainWindow()
    main_window._worker = None
    
    # Create and set up panels
    profile_panel = ProfilePanel(main_window.config_manager)
    main_window.left_layout.insertWidget(0, profile_panel)
    
    config_panel = ConfigPanel()
    main_window.center_layout.insertWidget(0, config_panel)
    
    preview_panel = MarkdownPreviewPanel()
    main_window.right_layout.insertWidget(0, preview_panel)
    
    # Setup worker related functions
    def _on_generation_started():
        if not main_window.current_config:
            from PySide6.QtWidgets import QMessageBox
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
        from repoinsight.gui.worker import DocumentationWorker
        main_window._worker = DocumentationWorker(main_window.current_config)
        
        # Connect worker signals
        main_window._worker.started.connect(
            lambda: main_window.status_label.setText("Documentation generation started...")
        )
        main_window._worker.progress.connect(lambda p, m: _update_progress(p, m))
        main_window._worker.finished.connect(lambda markdown: _on_generation_completed(markdown))
        main_window._worker.error.connect(lambda msg: _on_generation_error(msg))
        
        # Start worker
        main_window._worker.start()
    
    def _update_progress(percentage, message):
        main_window.progress_bar.setValue(percentage)
        main_window.progress_bar.setVisible(True)
        main_window.status_label.setText(message)
    
    def _on_generation_completed(markdown):
        main_window.progress_bar.setVisible(False)
        main_window.status_label.setText("Documentation generation completed")
        
        if markdown:
            # Emit signal with the generated markdown
            main_window.generation_completed.emit(markdown)
        else:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(
                main_window,
                "Generation Error",
                "Failed to generate documentation. Please check the logs for details.",
            )
    
    def _on_generation_error(message):
        main_window.progress_bar.setVisible(False)
        main_window.status_label.setText(f"Error: {message}")
        
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(
            main_window,
            "Generation Error",
            f"An error occurred during documentation generation:\n\n{message}",
        )
    
    # Attach methods to main window
    main_window._on_generation_started = _on_generation_started
    main_window._update_progress = _update_progress
    main_window._on_generation_completed = _on_generation_completed
    main_window._on_generation_error = _on_generation_error
    
    # Connect signals
    main_window.generation_started.connect(main_window._on_generation_started)
    main_window.generation_completed.connect(preview_panel.set_markdown)
    
    # Show the window
    main_window.show()
    
    # Schedule the Run action
    logger.info("Scheduling Run action")
    QTimer.singleShot(1000, lambda: test_run_action(main_window))
    
    # Run the application
    return app.exec()

def test_run_action(main_window):
    """Test clicking the Run button and then closing the window."""
    try:
        logger.info("Triggering Run action")
        main_window.run_action.trigger()
        
        # Schedule application close after a delay to let the operation start
        logger.info("Scheduling application close")
        QTimer.singleShot(3000, lambda: test_close_app(main_window))
    except Exception as e:
        logger.error(f"Error triggering run action: {e}")

def test_close_app(main_window):
    """Close the application window."""
    try:
        logger.info("Closing application")
        main_window.close()
        logger.info("Application closed successfully")
    except Exception as e:
        logger.error(f"Error closing application: {e}")


if __name__ == "__main__":
    logger.info("Starting RepoInsight GUI test for thread fix verification")
    sys.exit(run_test())
