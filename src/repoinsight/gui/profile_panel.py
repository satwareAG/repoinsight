"""
Profile management panel for RepoInsight GUI.

This module provides components for managing configuration profiles.
"""

import logging
from pathlib import Path
from typing import TYPE_CHECKING

from PySide6.QtCore import QModelIndex, QPoint, Qt, Signal
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QListView,
    QMenu,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from repoinsight.config.models import RepoInsightConfig

if TYPE_CHECKING:
    from repoinsight.config.yaml import ConfigManager

logger = logging.getLogger(__name__)


class ProfilePanel(QWidget):
    """
    Panel for managing configuration profiles.

    This panel displays a list of available profiles and provides
    controls for creating, selecting, duplicating, and deleting profiles.
    """

    # Signals
    profile_selected = Signal(RepoInsightConfig)
    profile_created = Signal(RepoInsightConfig)
    profile_deleted = Signal(str)  # Profile name

    def __init__(self, config_manager: 'ConfigManager', parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.config_manager = config_manager
        self.current_profile_name: str | None = None

        # Initialize UI
        self._init_ui()

        # Load profiles
        self._refresh_profiles()

    def _init_ui(self) -> None:
        """Initialize the UI components."""
        # Create main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)

        # Add header label
        header_label = QLabel("<b>Configuration Profiles</b>")
        main_layout.addWidget(header_label)

        # Add profile list
        self.profile_model = QStandardItemModel(self)
        self.profile_list = QListView()
        self.profile_list.setModel(self.profile_model)
        self.profile_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.profile_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.profile_list.clicked.connect(self._on_profile_clicked)
        self.profile_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.profile_list.customContextMenuRequested.connect(self._show_context_menu)
        main_layout.addWidget(self.profile_list)

        # Add button layout
        button_layout = QHBoxLayout()

        # Add profile button
        self.add_button = QPushButton("Add")
        self.add_button.setToolTip("Create a new profile")
        self.add_button.clicked.connect(self._create_profile)
        button_layout.addWidget(self.add_button)

        # Duplicate profile button
        self.duplicate_button = QPushButton("Duplicate")
        self.duplicate_button.setToolTip("Duplicate the selected profile")
        self.duplicate_button.clicked.connect(self._duplicate_profile)
        button_layout.addWidget(self.duplicate_button)

        # Delete profile button
        self.delete_button = QPushButton("Delete")
        self.delete_button.setToolTip("Delete the selected profile")
        self.delete_button.clicked.connect(self._delete_profile)
        button_layout.addWidget(self.delete_button)

        main_layout.addLayout(button_layout)

    def _refresh_profiles(self) -> None:
        """Refresh the list of available profiles."""
        self.profile_model.clear()

        # Get available profiles
        profiles = self.config_manager.get_available_profiles()

        # Add default profile
        default_item = QStandardItem("Default")
        default_item.setData("Default", Qt.ItemDataRole.UserRole)
        self.profile_model.appendRow(default_item)

        # Add other profiles
        for profile_name in profiles:
            if profile_name != "Default":  # Skip default if it's already in the list
                item = QStandardItem(profile_name)
                item.setData(profile_name, Qt.ItemDataRole.UserRole)
                self.profile_model.appendRow(item)

        # Select current profile if it exists
        if self.current_profile_name:
            self._select_profile_by_name(self.current_profile_name)
        else:
            # Select default profile
            self.profile_list.setCurrentIndex(self.profile_model.index(0, 0))
            self._on_profile_clicked(self.profile_model.index(0, 0))

    def _select_profile_by_name(self, profile_name: str) -> bool:
        """Select a profile by name."""
        for row in range(self.profile_model.rowCount()):
            item = self.profile_model.item(row)
            if item.data(Qt.ItemDataRole.UserRole) == profile_name:
                self.profile_list.setCurrentIndex(self.profile_model.index(row, 0))
                return True
        return False

    def _on_profile_clicked(self, index: QModelIndex) -> None:
        """Handle profile selection."""
        if not index.isValid():
            return

        profile_name = index.data(Qt.ItemDataRole.UserRole)
        if not profile_name:
            profile_name = index.data()

        self.current_profile_name = profile_name

        try:
            # Load the selected profile
            if profile_name == "Default":
                config = self.config_manager.load_default_config()
            else:
                config = self.config_manager.load_profile(profile_name)

            # Emit signal with loaded config
            self.profile_selected.emit(config)
        except Exception as e:
            logger.error(f"Error loading profile {profile_name}: {e}")
            QMessageBox.warning(
                self, "Profile Error", f"Error loading profile '{profile_name}': {str(e)}"
            )

    def _show_context_menu(self, position: QPoint) -> None:
        """Show context menu for the profile list."""
        index = self.profile_list.indexAt(position)
        if not index.isValid():
            return

        # Create context menu
        menu = QMenu(self)
        rename_action = menu.addAction("Rename")
        duplicate_action = menu.addAction("Duplicate")
        menu.addSeparator()
        delete_action = menu.addAction("Delete")

        # Show menu and handle result
        action = menu.exec_(self.profile_list.viewport().mapToGlobal(position))

        if action == rename_action:
            self._rename_profile(index)
        elif action == duplicate_action:
            self._duplicate_profile(index)
        elif action == delete_action:
            self._delete_profile(index)

    def _create_profile(self) -> None:
        """Create a new profile."""
        name, ok = QInputDialog.getText(self, "New Profile", "Enter profile name:")

        if ok and name:
            # Check if profile already exists
            if name in self.config_manager.get_available_profiles() or name == "Default":
                QMessageBox.warning(
                    self, "Profile Error", f"A profile named '{name}' already exists."
                )
                return

            # Create a new profile
            config = RepoInsightConfig(
                name=name,
                root_path=str(Path.cwd()),
            )

            # Save the profile
            self.config_manager.save_profile(config)

            # Refresh the list
            self._refresh_profiles()

            # Select the new profile
            self._select_profile_by_name(name)

            # Emit signal
            self.profile_created.emit(config)

    def _rename_profile(self, index: QModelIndex | None = None) -> None:
        """Rename the selected profile."""
        if index is None:
            index = self.profile_list.currentIndex()

        if not index.isValid():
            return

        profile_name = index.data(Qt.ItemDataRole.UserRole)
        if not profile_name:
            profile_name = index.data()

        # Don't allow renaming the default profile
        if profile_name == "Default":
            QMessageBox.warning(self, "Profile Error", "The default profile cannot be renamed.")
            return

        new_name, ok = QInputDialog.getText(
            self, "Rename Profile", "Enter new profile name:", text=profile_name
        )

        if ok and new_name and new_name != profile_name:
            # Check if profile already exists
            if new_name in self.config_manager.get_available_profiles() or new_name == "Default":
                QMessageBox.warning(
                    self, "Profile Error", f"A profile named '{new_name}' already exists."
                )
                return

            try:
                # Load the profile
                config = self.config_manager.load_profile(profile_name)

                # Delete the old profile
                self.config_manager.delete_profile(profile_name)

                # Update the name
                config.name = new_name

                # Save with new name
                self.config_manager.save_profile(config)

                # Update current profile name
                self.current_profile_name = new_name

                # Refresh the list
                self._refresh_profiles()

                # Emit signal
                self.profile_selected.emit(config)
            except Exception as e:
                logger.error(f"Error renaming profile {profile_name} to {new_name}: {e}")
                QMessageBox.warning(self, "Profile Error", f"Error renaming profile: {str(e)}")

    def _duplicate_profile(self, index: QModelIndex | None = None) -> None:
        """Duplicate the selected profile."""
        if index is None:
            index = self.profile_list.currentIndex()

        if not index.isValid():
            return

        profile_name = index.data(Qt.ItemDataRole.UserRole)
        if not profile_name:
            profile_name = index.data()

        # Load the profile to duplicate
        try:
            if profile_name == "Default":
                config = self.config_manager.load_default_config()
            else:
                config = self.config_manager.load_profile(profile_name)

            # Generate a new name
            new_name = f"{profile_name} (Copy)"
            count = 1
            while new_name in self.config_manager.get_available_profiles() or new_name == "Default":
                count += 1
                new_name = f"{profile_name} (Copy {count})"

            # Update the name
            config.name = new_name

            # Save as a new profile
            self.config_manager.save_profile(config)

            # Refresh the list
            self._refresh_profiles()

            # Select the new profile
            self._select_profile_by_name(new_name)

            # Emit signal
            self.profile_created.emit(config)
        except Exception as e:
            logger.error(f"Error duplicating profile {profile_name}: {e}")
            QMessageBox.warning(self, "Profile Error", f"Error duplicating profile: {str(e)}")

    def _delete_profile(self, index: QModelIndex | None = None) -> None:
        """Delete the selected profile."""
        if index is None:
            index = self.profile_list.currentIndex()

        if not index.isValid():
            return

        profile_name = index.data(Qt.ItemDataRole.UserRole)
        if not profile_name:
            profile_name = index.data()

        # Don't allow deleting the default profile
        if profile_name == "Default":
            QMessageBox.warning(self, "Profile Error", "The default profile cannot be deleted.")
            return

        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Delete Profile",
            f"Are you sure you want to delete the profile '{profile_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Delete the profile
                success = self.config_manager.delete_profile(profile_name)

                if success:
                    # Refresh the list
                    self._refresh_profiles()

                    # Emit signal
                    self.profile_deleted.emit(profile_name)
                else:
                    QMessageBox.warning(
                        self, "Profile Error", f"Failed to delete profile '{profile_name}'."
                    )
            except Exception as e:
                logger.error(f"Error deleting profile {profile_name}: {e}")
                QMessageBox.warning(self, "Profile Error", f"Error deleting profile: {str(e)}")
