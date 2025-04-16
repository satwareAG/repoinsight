"""
GUI package for RepoInsight.

This package provides the graphical user interface for the application.
"""

from repoinsight.gui.app import run_app
from repoinsight.gui.config_panel import ConfigPanel
from repoinsight.gui.main_window import MainWindow
from repoinsight.gui.preview_panel import MarkdownPreviewPanel
from repoinsight.gui.profile_panel import ProfilePanel
from repoinsight.gui.worker import AsyncWorker, DocumentationWorker

__all__ = [
    "run_app",
    "MainWindow",
    "ProfilePanel",
    "ConfigPanel",
    "MarkdownPreviewPanel",
    "AsyncWorker",
    "DocumentationWorker",
]
