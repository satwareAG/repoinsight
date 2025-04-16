"""
Main GUI application module for RepoInsight.

This module provides the main application entry point for the GUI.
"""

import logging
import sys
from pathlib import Path
from typing import List, Optional

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QTabWidget,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from repoinsight import __version__
from repoinsight.config.yaml import ConfigManager

# Set up logging
logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """
    Main window for the RepoInsight application.
    """
    
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle(f"RepoInsight v{__version__}")
        self.setMinimumSize(1200, 800)
        
        # Initialize UI
        self._create_actions()
        self._create_menu_bar()
        self._create_tool_bar()
        self._create_status_bar()
        self._create_central_widget()
        
        # Initialize config manager
        self.config_manager = ConfigManager()
        
        # Show the window
        self.show()
        
    def _create_actions(self):
        """Create actions for menus and toolbars."""
        # File actions
        self.open_action = QAction("Open Repository...", self)
        self.open_action.setStatusTip("Open a repository")
        self.open_action.triggered.connect(self._open_repository)
        
        self.save_action = QAction("Save Output...", self)
        self.save_action.setStatusTip("Save generated markdown")
        self.save_action.triggered.connect(self._save_output)
        
        self.exit_action = QAction("Exit", self)
        self.exit_action.setStatusTip("Exit the application")
        self.exit_action.triggered.connect(self.close)
        
        # Run actions
        self.run_action = QAction("Run", self)
        self.run_action.setStatusTip("Run the documentation generation")
        self.run_action.triggered.connect(self._run_documentation)
        
        # Help actions
        self.about_action = QAction("About", self)
        self.about_action.setStatusTip("Show about dialog")
        self.about_action.triggered.connect(self._show_about_dialog)
        
    def _create_menu_bar(self):
        """Create the menu bar."""
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)
        
        # Run menu
        run_menu = menu_bar.addMenu("Run")
        run_menu.addAction(self.run_action)
        
        # Help menu
        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.about_action)
        
    def _create_tool_bar(self):
        """Create the toolbar."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        
        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()
        toolbar.addAction(self.run_action)
        
    def _create_status_bar(self):
        """Create the status bar."""
        self.statusBar().showMessage("Ready")
        
    def _create_central_widget(self):
        """Create the central widget."""
        # Create a main vertical layout
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        
        # Add tabs
        self.setup_tab = QWidget()
        self.preview_tab = QWidget()
        
        self.tab_widget.addTab(self.setup_tab, "Setup")
        self.tab_widget.addTab(self.preview_tab, "Preview")
        
        # Add tab widget to main layout
        main_layout.addWidget(self.tab_widget)
        
        # Set central widget
        self.setCentralWidget(central_widget)
        
    def _open_repository(self):
        """Open a repository directory."""
        directory = QFileDialog.getExistingDirectory(
            self, "Select Repository Directory"
        )
        
        if directory:
            self.statusBar().showMessage(f"Repository: {directory}")
            
    def _save_output(self):
        """Save the generated output."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Output", "", "Markdown Files (*.md);;All Files (*)"
        )
        
        if file_path:
            self.statusBar().showMessage(f"Output saved to: {file_path}")
            
    def _run_documentation(self):
        """Run the documentation generation process."""
        self.statusBar().showMessage("Running documentation generation...")
        
    def _show_about_dialog(self):
        """Show the about dialog."""
        QMessageBox.about(
            self,
            "About RepoInsight",
            f"<h3>RepoInsight v{__version__}</h3>"
            "<p>Automated documentation for Git repositories with AI-enhanced descriptions.</p>"
            "<p>© 2025 satware</p>",
        )
        
    def closeEvent(self, event):
        """Handle window close event."""
        event.accept()


def run_app():
    """
    Run the RepoInsight GUI application.
    
    Returns:
        Exit code
    """
    app = QApplication(sys.argv)
    main_window = MainWindow()
    return app.exec()


if __name__ == "__main__":
    sys.exit(run_app())
