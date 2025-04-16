"""
Configuration panel for RepoInsight GUI.

This module provides a widget for editing the configuration settings.
"""

import logging
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QPlainTextEdit,
    QPushButton,
    QScrollArea,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from repoinsight.config.models import RepoInsightConfig

logger = logging.getLogger(__name__)


class ConfigPanel(QWidget):
    """
    Panel for editing configuration settings.

    This panel provides UI for configuring all aspects of repository scanning
    and documentation generation.
    """

    # Signals
    config_changed = Signal(RepoInsightConfig)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.config = None

        # Initialize UI
        self._init_ui()

    def _init_ui(self) -> None:
        """Initialize the UI components."""
        # Create main layout with scroll area
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)

        # Create scroll area for configuration
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_layout.addWidget(scroll_area)

        # Create container widget for scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(4, 4, 4, 4)
        scroll_area.setWidget(scroll_widget)

        # Add header label
        header_label = QLabel("<b>Repository Configuration</b>")
        scroll_layout.addWidget(header_label)

        # Create tab widget for different config sections
        self.tab_widget = QTabWidget()
        scroll_layout.addWidget(self.tab_widget)

        # Create tabs for different sections
        self._create_basic_tab()
        self._create_files_tab()
        self._create_llm_tab()
        self._create_output_tab()

        # Add save button at the bottom
        save_button = QPushButton("Apply Changes")
        save_button.clicked.connect(self._apply_changes)
        scroll_layout.addWidget(save_button)

    def _create_basic_tab(self) -> None:
        """Create the basic settings tab."""
        basic_tab = QWidget()
        layout = QVBoxLayout(basic_tab)

        # Repository settings group
        repo_group = QGroupBox("Repository Settings")
        repo_layout = QFormLayout(repo_group)

        # Name field
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Project name")
        repo_layout.addRow("Name:", self.name_edit)

        # Root path field with browse button
        root_path_widget = QWidget()
        root_path_layout = QHBoxLayout(root_path_widget)
        root_path_layout.setContentsMargins(0, 0, 0, 0)

        self.root_path_edit = QLineEdit()
        self.root_path_edit.setPlaceholderText("Repository root path")
        root_path_layout.addWidget(self.root_path_edit, 1)

        root_path_browse = QPushButton("Browse...")
        root_path_browse.clicked.connect(self._browse_root_path)
        root_path_layout.addWidget(root_path_browse)

        repo_layout.addRow("Root Path:", root_path_widget)

        # Output path field with browse button
        output_path_widget = QWidget()
        output_path_layout = QHBoxLayout(output_path_widget)
        output_path_layout.setContentsMargins(0, 0, 0, 0)

        self.output_path_edit = QLineEdit()
        self.output_path_edit.setPlaceholderText("Output file path (optional)")
        output_path_layout.addWidget(self.output_path_edit, 1)

        output_path_browse = QPushButton("Browse...")
        output_path_browse.clicked.connect(self._browse_output_path)
        output_path_layout.addWidget(output_path_browse)

        repo_layout.addRow("Output Path:", output_path_widget)

        # Cache path field
        self.cache_path_edit = QLineEdit()
        self.cache_path_edit.setPlaceholderText(".repoinsight_cache")
        repo_layout.addRow("Cache Path:", self.cache_path_edit)

        layout.addWidget(repo_group)
        layout.addStretch()

        self.tab_widget.addTab(basic_tab, "Basic")

    def _create_files_tab(self) -> None:
        """Create the file patterns tab."""
        files_tab = QWidget()
        layout = QVBoxLayout(files_tab)

        # Scan directories group
        scan_group = QGroupBox("Scan Directories")
        scan_layout = QVBoxLayout(scan_group)

        self.scan_dirs_list = QListWidget()
        scan_layout.addWidget(self.scan_dirs_list)

        scan_buttons_layout = QHBoxLayout()
        add_scan_button = QPushButton("Add")
        add_scan_button.clicked.connect(self._add_scan_dir)
        scan_buttons_layout.addWidget(add_scan_button)

        remove_scan_button = QPushButton("Remove")
        remove_scan_button.clicked.connect(self._remove_scan_dir)
        scan_buttons_layout.addWidget(remove_scan_button)

        scan_layout.addLayout(scan_buttons_layout)
        layout.addWidget(scan_group)

        # Exclude directories group
        exclude_group = QGroupBox("Exclude Directories")
        exclude_layout = QVBoxLayout(exclude_group)

        self.exclude_dirs_list = QListWidget()
        exclude_layout.addWidget(self.exclude_dirs_list)

        exclude_buttons_layout = QHBoxLayout()
        add_exclude_button = QPushButton("Add")
        add_exclude_button.clicked.connect(self._add_exclude_dir)
        exclude_buttons_layout.addWidget(add_exclude_button)

        remove_exclude_button = QPushButton("Remove")
        remove_exclude_button.clicked.connect(self._remove_exclude_dir)
        exclude_buttons_layout.addWidget(remove_exclude_button)

        exclude_layout.addLayout(exclude_buttons_layout)
        layout.addWidget(exclude_group)

        # Include file patterns group
        include_group = QGroupBox("Include File Patterns")
        include_layout = QVBoxLayout(include_group)

        self.include_patterns_list = QListWidget()
        include_layout.addWidget(self.include_patterns_list)

        include_buttons_layout = QHBoxLayout()
        add_include_button = QPushButton("Add")
        add_include_button.clicked.connect(self._add_include_pattern)
        include_buttons_layout.addWidget(add_include_button)

        remove_include_button = QPushButton("Remove")
        remove_include_button.clicked.connect(self._remove_include_pattern)
        include_buttons_layout.addWidget(remove_include_button)

        include_layout.addLayout(include_buttons_layout)
        layout.addWidget(include_group)

        # Exclude file patterns group
        exclude_patterns_group = QGroupBox("Exclude File Patterns")
        exclude_patterns_layout = QVBoxLayout(exclude_patterns_group)

        self.exclude_patterns_list = QListWidget()
        exclude_patterns_layout.addWidget(self.exclude_patterns_list)

        exclude_patterns_buttons_layout = QHBoxLayout()
        add_exclude_pattern_button = QPushButton("Add")
        add_exclude_pattern_button.clicked.connect(self._add_exclude_pattern)
        exclude_patterns_buttons_layout.addWidget(add_exclude_pattern_button)

        remove_exclude_pattern_button = QPushButton("Remove")
        remove_exclude_pattern_button.clicked.connect(self._remove_exclude_pattern)
        exclude_patterns_buttons_layout.addWidget(remove_exclude_pattern_button)

        exclude_patterns_layout.addLayout(exclude_patterns_buttons_layout)
        layout.addWidget(exclude_patterns_group)

        self.tab_widget.addTab(files_tab, "Files")

    def _create_llm_tab(self) -> None:
        """Create the LLM settings tab."""
        llm_tab = QWidget()
        layout = QVBoxLayout(llm_tab)

        # LLM group
        llm_group = QGroupBox("LLM Integration")
        llm_layout = QFormLayout(llm_group)

        # Enabled checkbox
        self.llm_enabled_check = QCheckBox("Enable LLM Integration")
        llm_layout.addRow("", self.llm_enabled_check)

        # Provider field
        self.llm_provider_combo = QComboBox()
        self.llm_provider_combo.addItems(["cortex", "openai", "ollama", "local"])
        llm_layout.addRow("Provider:", self.llm_provider_combo)

        # API Base URL field
        self.llm_api_url_edit = QLineEdit()
        self.llm_api_url_edit.setPlaceholderText("http://localhost:8000/v1")
        llm_layout.addRow("API Base URL:", self.llm_api_url_edit)

        # API Key field
        self.llm_api_key_edit = QLineEdit()
        self.llm_api_key_edit.setPlaceholderText("API key (optional)")
        self.llm_api_key_edit.setEchoMode(QLineEdit.EchoMode.Password)
        llm_layout.addRow("API Key:", self.llm_api_key_edit)

        # Model field
        self.llm_model_edit = QLineEdit()
        self.llm_model_edit.setPlaceholderText("llama3")
        llm_layout.addRow("Model:", self.llm_model_edit)

        # Temperature field
        self.llm_temperature_spin = QDoubleSpinBox()
        self.llm_temperature_spin.setRange(0.0, 1.0)
        self.llm_temperature_spin.setSingleStep(0.1)
        self.llm_temperature_spin.setValue(0.3)
        llm_layout.addRow("Temperature:", self.llm_temperature_spin)

        # Max tokens field
        self.llm_max_tokens_spin = QSpinBox()
        self.llm_max_tokens_spin.setRange(1, 4000)
        self.llm_max_tokens_spin.setValue(500)
        llm_layout.addRow("Max Tokens:", self.llm_max_tokens_spin)

        # Timeout field
        self.llm_timeout_spin = QSpinBox()
        self.llm_timeout_spin.setRange(1, 300)
        self.llm_timeout_spin.setValue(30)
        llm_layout.addRow("Timeout (s):", self.llm_timeout_spin)

        # Cache enabled checkbox
        self.llm_cache_enabled_check = QCheckBox("Enable Caching")
        llm_layout.addRow("", self.llm_cache_enabled_check)

        # System prompt template
        llm_layout.addRow("System Prompt Template:", QLabel())
        self.llm_system_prompt_edit = QPlainTextEdit()
        self.llm_system_prompt_edit.setPlaceholderText(
            "Analyze the following {language} code and provide a concise description..."
        )
        self.llm_system_prompt_edit.setMinimumHeight(100)
        llm_layout.addRow("", self.llm_system_prompt_edit)

        layout.addWidget(llm_group)
        layout.addStretch()

        self.tab_widget.addTab(llm_tab, "LLM")

    def _create_output_tab(self) -> None:
        """Create the output settings tab."""
        output_tab = QWidget()
        layout = QVBoxLayout(output_tab)

        # Output options group
        output_group = QGroupBox("Output Options")
        output_layout = QFormLayout(output_group)

        # Include TOC checkbox
        self.include_toc_check = QCheckBox()
        self.include_toc_check.setChecked(True)
        output_layout.addRow("Include Table of Contents:", self.include_toc_check)

        # Include metadata checkbox
        self.include_metadata_check = QCheckBox()
        self.include_metadata_check.setChecked(True)
        output_layout.addRow("Include Metadata:", self.include_metadata_check)

        # Include file stats checkbox
        self.include_file_stats_check = QCheckBox()
        self.include_file_stats_check.setChecked(True)
        output_layout.addRow("Include File Statistics:", self.include_file_stats_check)

        # Include commit info checkbox
        self.include_commit_info_check = QCheckBox()
        self.include_commit_info_check.setChecked(True)
        output_layout.addRow("Include Commit Information:", self.include_commit_info_check)

        # Syntax highlighting checkbox
        self.syntax_highlighting_check = QCheckBox()
        self.syntax_highlighting_check.setChecked(True)
        output_layout.addRow("Syntax Highlighting:", self.syntax_highlighting_check)

        layout.addWidget(output_group)

        # Processing group
        processing_group = QGroupBox("Processing Options")
        processing_layout = QFormLayout(processing_group)

        # Max concurrent tasks
        self.max_concurrent_tasks_spin = QSpinBox()
        self.max_concurrent_tasks_spin.setRange(1, 16)
        self.max_concurrent_tasks_spin.setValue(4)
        processing_layout.addRow("Max Concurrent Tasks:", self.max_concurrent_tasks_spin)

        # Chunk size
        self.chunk_size_spin = QSpinBox()
        self.chunk_size_spin.setRange(1024, 65536)
        self.chunk_size_spin.setSingleStep(1024)
        self.chunk_size_spin.setValue(8192)
        processing_layout.addRow("Chunk Size (bytes):", self.chunk_size_spin)

        layout.addWidget(processing_group)
        layout.addStretch()

        self.tab_widget.addTab(output_tab, "Output")

    def _browse_root_path(self) -> None:
        """Browse for repository root path."""
        directory = QFileDialog.getExistingDirectory(self, "Select Repository Directory")
        if directory:
            self.root_path_edit.setText(directory)

    def _browse_output_path(self) -> None:
        """Browse for output file path."""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Output", "", "Markdown Files (*.md);;All Files (*)"
        )
        if file_path:
            self.output_path_edit.setText(file_path)

    def _add_scan_dir(self) -> None:
        """Add a scan directory."""
        if not self.config:
            return

        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory to Scan", str(Path(self.root_path_edit.text()))
        )

        if directory:
            # Convert to relative path if possible
            try:
                root_path = Path(self.root_path_edit.text())
                scan_path = Path(directory)
                relative_path = scan_path.relative_to(root_path)
                directory = str(relative_path)
            except ValueError:
                # Not a relative path, use absolute
                pass

            # Add to list if not already present
            if directory not in [
                self.scan_dirs_list.item(i).text() for i in range(self.scan_dirs_list.count())
            ]:
                self.scan_dirs_list.addItem(directory)

    def _remove_scan_dir(self) -> None:
        """Remove a scan directory."""
        selected_items = self.scan_dirs_list.selectedItems()
        for item in selected_items:
            self.scan_dirs_list.takeItem(self.scan_dirs_list.row(item))

    def _add_exclude_dir(self) -> None:
        """Add an exclude directory."""
        directory = QFileDialog.getExistingDirectory(
            self, "Select Directory to Exclude", str(Path(self.root_path_edit.text()))
        )

        if directory:
            # Convert to relative path if possible
            try:
                root_path = Path(self.root_path_edit.text())
                exclude_path = Path(directory)
                relative_path = exclude_path.relative_to(root_path)
                directory = str(relative_path)
            except ValueError:
                # Just get the directory name in this case
                directory = Path(directory).name

            # Add to list if not already present
            if directory not in [
                self.exclude_dirs_list.item(i).text()
                for i in range(self.exclude_dirs_list.count())
            ]:
                self.exclude_dirs_list.addItem(directory)

    def _remove_exclude_dir(self) -> None:
        """Remove an exclude directory."""
        selected_items = self.exclude_dirs_list.selectedItems()
        for item in selected_items:
            self.exclude_dirs_list.takeItem(self.exclude_dirs_list.row(item))

    def _add_include_pattern(self) -> None:
        """Add an include pattern."""
        # Simple implementation using an input dialog
        pattern, ok = QInputDialog.getText(
            self, "Add Include Pattern", "Enter glob pattern to include files:", text="*.py"
        )

        if ok and pattern:
            # Add to list if not already present
            if pattern not in [
                self.include_patterns_list.item(i).text()
                for i in range(self.include_patterns_list.count())
            ]:
                self.include_patterns_list.addItem(pattern)

    def _remove_include_pattern(self) -> None:
        """Remove an include pattern."""
        selected_items = self.include_patterns_list.selectedItems()
        for item in selected_items:
            self.include_patterns_list.takeItem(self.include_patterns_list.row(item))

    def _add_exclude_pattern(self) -> None:
        """Add an exclude pattern."""
        # Simple implementation using an input dialog
        pattern, ok = QInputDialog.getText(
            self, "Add Exclude Pattern", "Enter glob pattern to exclude files:", text="*.pyc"
        )

        if ok and pattern:
            # Add to list if not already present
            if pattern not in [
                self.exclude_patterns_list.item(i).text()
                for i in range(self.exclude_patterns_list.count())
            ]:
                self.exclude_patterns_list.addItem(pattern)

    def _remove_exclude_pattern(self) -> None:
        """Remove an exclude pattern."""
        selected_items = self.exclude_patterns_list.selectedItems()
        for item in selected_items:
            self.exclude_patterns_list.takeItem(self.exclude_patterns_list.row(item))

    def set_config(self, config) -> None:
        """Set the configuration to edit."""
        self.config = config

        if config:
            # Update UI with config values
            self._update_ui_from_config()

    def _update_ui_from_config(self) -> None:
        """Update UI elements with values from the current config."""
        if not self.config:
            return

        # Basic tab
        self.name_edit.setText(self.config.name)
        self.root_path_edit.setText(self.config.root_path)
        self.output_path_edit.setText(self.config.output_path or "")
        self.cache_path_edit.setText(self.config.cache_path)

        # Files tab
        self.scan_dirs_list.clear()
        self.scan_dirs_list.addItems(self.config.scan_directories)

        self.exclude_dirs_list.clear()
        self.exclude_dirs_list.addItems(self.config.exclude_directories)

        self.include_patterns_list.clear()
        self.include_patterns_list.addItems(self.config.file_patterns.include)

        self.exclude_patterns_list.clear()
        self.exclude_patterns_list.addItems(self.config.file_patterns.exclude)

        # LLM tab
        self.llm_enabled_check.setChecked(self.config.llm.enabled)

        index = self.llm_provider_combo.findText(self.config.llm.provider)
        if index >= 0:
            self.llm_provider_combo.setCurrentIndex(index)

        self.llm_api_url_edit.setText(self.config.llm.api_base_url)
        if self.config.llm.api_key:
            self.llm_api_key_edit.setText(self.config.llm.api_key)
        self.llm_model_edit.setText(self.config.llm.model)
        self.llm_temperature_spin.setValue(self.config.llm.temperature)
        self.llm_max_tokens_spin.setValue(self.config.llm.max_tokens)
        self.llm_timeout_spin.setValue(self.config.llm.timeout)
        self.llm_cache_enabled_check.setChecked(self.config.llm.cache_enabled)
        self.llm_system_prompt_edit.setPlainText(self.config.llm.system_prompt_template)

        # Output tab
        self.include_toc_check.setChecked(self.config.output.include_toc)
        self.include_metadata_check.setChecked(self.config.output.include_metadata)
        self.include_file_stats_check.setChecked(self.config.output.include_file_stats)
        self.include_commit_info_check.setChecked(self.config.output.include_commit_info)
        self.syntax_highlighting_check.setChecked(self.config.output.syntax_highlighting)
        self.max_concurrent_tasks_spin.setValue(self.config.processing.max_concurrent_tasks)
        self.chunk_size_spin.setValue(self.config.processing.chunk_size)

    def _apply_changes(self) -> None:
        """Apply changes to the configuration."""
        if not self.config:
            return

        # Update basic settings
        self.config.name = self.name_edit.text()
        self.config.root_path = self.root_path_edit.text()

        if self.output_path_edit.text():
            self.config.output_path = self.output_path_edit.text()
        else:
            self.config.output_path = None

        self.config.cache_path = self.cache_path_edit.text()

        # Update scan directories
        self.config.scan_directories = [
            self.scan_dirs_list.item(i).text() for i in range(self.scan_dirs_list.count())
        ]

        # Update exclude directories
        self.config.exclude_directories = [
            self.exclude_dirs_list.item(i).text() for i in range(self.exclude_dirs_list.count())
        ]

        # Update file patterns
        self.config.file_patterns.include = [
            self.include_patterns_list.item(i).text()
            for i in range(self.include_patterns_list.count())
        ]

        self.config.file_patterns.exclude = [
            self.exclude_patterns_list.item(i).text()
            for i in range(self.exclude_patterns_list.count())
        ]

        # Update LLM settings
        self.config.llm.enabled = self.llm_enabled_check.isChecked()
        self.config.llm.provider = self.llm_provider_combo.currentText()
        self.config.llm.api_base_url = self.llm_api_url_edit.text()

        # Only update API key if it was changed (non-empty)
        if self.llm_api_key_edit.text():
            self.config.llm.api_key = self.llm_api_key_edit.text()

        self.config.llm.model = self.llm_model_edit.text()
        self.config.llm.temperature = self.llm_temperature_spin.value()
        self.config.llm.max_tokens = self.llm_max_tokens_spin.value()
        self.config.llm.timeout = self.llm_timeout_spin.value()
        self.config.llm.cache_enabled = self.llm_cache_enabled_check.isChecked()
        self.config.llm.system_prompt_template = self.llm_system_prompt_edit.toPlainText()

        # Update output settings
        self.config.output.include_toc = self.include_toc_check.isChecked()
        self.config.output.include_metadata = self.include_metadata_check.isChecked()
        self.config.output.include_file_stats = self.include_file_stats_check.isChecked()
        self.config.output.include_commit_info = self.include_commit_info_check.isChecked()
        self.config.output.syntax_highlighting = self.syntax_highlighting_check.isChecked()

        # Update processing settings
        self.config.processing.max_concurrent_tasks = self.max_concurrent_tasks_spin.value()
        self.config.processing.chunk_size = self.chunk_size_spin.value()

        # Emit signal with updated config
        self.config_changed.emit(self.config)
