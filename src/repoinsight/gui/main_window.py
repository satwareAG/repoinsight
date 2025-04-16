"""
Main window implementation for RepoInsight GUI.

This module provides the main window of the application with a 3-panel layout.
"""

import logging
from pathlib import Path

from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QAction, QCloseEvent
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSplitter,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from repoinsight import __version__
from repoinsight.config.models import RepoInsightConfig
from repoinsight.config.yaml import ConfigManager

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """
    Main window for the RepoInsight application with 3-panel layout.
    """

    # Signals
    config_changed = Signal(RepoInsightConfig)
    repository_opened = Signal(Path)
    generation_started = Signal()
    generation_completed = Signal(str)  # Markdown content

    def __init__(self) -> None:
        super().__init__()

        # Set window properties
        self.setWindowTitle(f"RepoInsight v{__version__}")
        self.setMinimumSize(1200, 800)

        # Initialize config manager
        self.config_manager = ConfigManager()
        self.current_config = None

        # Initialize UI
        self._create_actions()
        self._create_menu_bar()
        self._create_tool_bar()
        self._create_status_bar()
        self._create_central_widget()

        # Show the window
        self.show()

        # Load default configuration
        self.current_config = self.config_manager.load_default_config()
        self.config_changed.emit(self.current_config)

    def _create_actions(self) -> None:
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

        # Profile actions
        self.new_profile_action = QAction("New Profile", self)
        self.new_profile_action.setStatusTip("Create a new configuration profile")
        self.new_profile_action.triggered.connect(self._new_profile)

        self.save_profile_action = QAction("Save Profile", self)
        self.save_profile_action.setStatusTip("Save current configuration profile")
        self.save_profile_action.triggered.connect(self._save_profile)

        # Run actions
        self.run_action = QAction("Run", self)
        self.run_action.setStatusTip("Run the documentation generation")
        self.run_action.triggered.connect(self._run_documentation)

        # Help actions
        self.about_action = QAction("About", self)
        self.about_action.setStatusTip("Show about dialog")
        self.about_action.triggered.connect(self._show_about_dialog)

    def _create_menu_bar(self) -> None:
        """Create the menu bar."""
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        # Profile menu
        profile_menu = menu_bar.addMenu("Profiles")
        profile_menu.addAction(self.new_profile_action)
        profile_menu.addAction(self.save_profile_action)

        # Run menu
        run_menu = menu_bar.addMenu("Run")
        run_menu.addAction(self.run_action)

        # Help menu
        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction(self.about_action)

    def _create_tool_bar(self) -> None:
        """Create the toolbar."""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(self.open_action)
        toolbar.addAction(self.save_action)
        toolbar.addSeparator()
        toolbar.addAction(self.run_action)

    def _create_status_bar(self) -> None:
        """Create the status bar with progress reporting."""
        # Create status bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

        # Add status label
        self.status_label = QLabel("Ready")
        status_bar.addWidget(self.status_label, 1)

        # Add progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setVisible(False)
        status_bar.addWidget(self.progress_bar, 2)

        # Add settings button
        self.settings_button = QPushButton("Settings")
        self.settings_button.setMaximumWidth(100)
        self.settings_button.clicked.connect(self._show_settings)
        status_bar.addPermanentWidget(self.settings_button)

    def _create_central_widget(self) -> None:
        """Create the central widget with 3-panel layout."""
        # Create main container
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Create main horizontal splitter
        self.main_splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(self.main_splitter)

        # Create left panel (Profiles)
        self.left_panel = QWidget()
        self.left_layout = QVBoxLayout(self.left_panel)
        self.left_layout.setContentsMargins(4, 4, 4, 4)

        # Left panel will be populated with profile list
        self.left_label = QLabel("Profiles")
        self.left_layout.addWidget(self.left_label)
        self.left_layout.addStretch()

        # Create center panel (Configuration)
        self.center_panel = QWidget()
        self.center_layout = QVBoxLayout(self.center_panel)
        self.center_layout.setContentsMargins(4, 4, 4, 4)

        # Center panel will be populated with configuration options
        self.center_label = QLabel("Configuration")
        self.center_layout.addWidget(self.center_label)
        self.center_layout.addStretch()

        # Create right panel (Preview)
        self.right_panel = QWidget()
        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setContentsMargins(4, 4, 4, 4)

        # Right panel will be populated with markdown preview
        self.right_label = QLabel("Preview")
        self.right_layout.addWidget(self.right_label)
        self.right_layout.addStretch()

        # Add panels to splitter
        self.main_splitter.addWidget(self.left_panel)
        self.main_splitter.addWidget(self.center_panel)
        self.main_splitter.addWidget(self.right_panel)

        # Set initial sizes (20% / 40% / 40%)
        self.main_splitter.setSizes([200, 400, 400])

        # Set central widget
        self.setCentralWidget(central_widget)

    def _open_repository(self) -> None:
        """Open a repository directory."""
        directory = QFileDialog.getExistingDirectory(self, "Select Repository Directory")

        if directory:
            self.status_label.setText(f"Repository: {directory}")

            # Update configuration
            if self.current_config:
                self.current_config.root_path = directory
                self.config_changed.emit(self.current_config)

            # Emit repository opened signal
            self.repository_opened.emit(Path(directory))

    def _save_output(self) -> None:
        """Save the generated output."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Output", "", "Markdown Files (*.md);;All Files (*)"
        )

        if file_path:
            # In a real implementation, we would get the markdown content
            # from the preview panel and save it
            self.status_label.setText(f"Output saved to: {file_path}")

    def _run_documentation(self) -> None:
        """Run the documentation generation process."""
        if not self.current_config:
            QMessageBox.warning(
                self,
                "Configuration Error",
                "No configuration available. Please open a repository first.",
            )
            return

        self.status_label.setText("Running documentation generation...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

        # In a real implementation, we would start the documentation
        # generation process asynchronously

        # Emit generation started signal
        self.generation_started.emit()

        # For demonstration purposes, we'll simulate progress
        # In a real implementation, this would be handled by a worker thread
        self.progress_bar.setValue(100)
        self.status_label.setText("Documentation generation completed")

        # Emit generation completed signal with placeholder content
        self.generation_completed.emit(
            "# Generated Documentation\n\nThis is a placeholder for the generated documentation."
        )

    def _show_about_dialog(self) -> None:
        """Show the about dialog."""
        QMessageBox.about(
            self,
            "About RepoInsight",
            f"<h3>RepoInsight v{__version__}</h3>"
            "<p>Automated documentation for Git repositories with AI-enhanced descriptions.</p>"
            "<p>© 2025 satware</p>",
        )

    def _new_profile(self) -> None:
        """Create a new configuration profile."""
        # In a real implementation, we would show a dialog to get the profile name
        from PySide6.QtWidgets import QInputDialog

        name, ok = QInputDialog.getText(self, "New Profile", "Enter profile name:")

        if ok and name:
            # Create a new profile
            self.current_config = RepoInsightConfig(
                name=name,
                root_path=str(Path.cwd()),
            )
            self.config_changed.emit(self.current_config)
            self.status_label.setText(f"Created new profile: {name}")

    def _save_profile(self) -> None:
        """Save the current configuration profile."""
        if not self.current_config:
            QMessageBox.warning(self, "Profile Error", "No profile to save.")
            return

        # Save the profile
        self.config_manager.save_profile(self.current_config)
        self.status_label.setText(f"Saved profile: {self.current_config.name}")

    def _show_settings(self) -> None:
        """Show the application settings dialog."""
        QMessageBox.information(self, "Settings", "Settings dialog would be shown here.")

    def closeEvent(self, event: QCloseEvent) -> None:  # noqa: N802
        """Handle window close event."""
        # In a real implementation, we would check for unsaved changes
        event.accept()
