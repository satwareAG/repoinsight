"""
Worker classes for asynchronous operations in the RepoInsight GUI.

This module provides worker classes for running long-running tasks
asynchronously in the GUI.
"""

import asyncio
import logging
from typing import Never

from PySide6.QtCore import QObject, QThread, Signal, Slot

from repoinsight.config.models import RepoInsightConfig
from repoinsight.core.engine import ProcessingEngine

logger = logging.getLogger(__name__)


class AsyncWorker(QObject):
    """
    Base worker class for asynchronous operations.

    This class provides a foundation for running asyncio tasks in a separate thread.
    """

    # Signals
    started = Signal()
    progress = Signal(int, str)  # Progress percentage, status message
    finished = Signal(object)  # Result object
    error = Signal(str)  # Error message

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._running = False
        self._loop = None
        self._thread = None
        self._task = None

    def is_running(self) -> bool:
        """Check if the worker is currently running."""
        return self._running

    def start(self) -> None:
        """Start the worker in a separate thread."""
        if self._running:
            return

        # Create a new thread
        self._thread = QThread()
        self.moveToThread(self._thread)

        # Connect signals
        self._thread.started.connect(self._run)

        # Start the thread
        self._running = True
        self._thread.start()

    def stop(self) -> None:
        """Stop the worker."""
        if not self._running:
            return

        self._running = False

        # Cancel the running task if it exists
        if self._loop and self._task and not self._task.done():
            logger.debug("Cancelling running asyncio task")
            self._loop.call_soon_threadsafe(self._task.cancel)

        # Clean up thread
        if self._thread:
            self._thread.quit()
            self._thread.wait()
            self._thread = None

    @Slot()
    def _run(self) -> None:
        """Worker thread entry point. Creates an event loop and runs the task."""
        try:
            # Create a new event loop for this thread
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)

            # Emit started signal
            self.started.emit()

            # Create and run the task
            self._task = self._loop.create_task(self._run_task())
            result = self._loop.run_until_complete(self._task)

            # Emit finished signal
            self.finished.emit(result)
        except asyncio.CancelledError:
            logger.info("Worker task was cancelled")
            self.error.emit("Operation was cancelled")
        except Exception as e:
            logger.exception("Error in worker thread")
            self.error.emit(str(e))
        finally:
            # Clean up
            self._running = False
            self._task = None
            if self._loop and self._loop.is_running():
                self._loop.stop()
            if self._loop and not self._loop.is_closed():
                self._loop.close()
            self._loop = None

    async def _run_task(self) -> Never:
        """Run the actual task. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement _run_task")


class DocumentationWorker(AsyncWorker):
    """
    Worker for generating documentation.

    This worker runs the ProcessingEngine asynchronously to generate
    documentation based on the provided configuration.
    """

    def __init__(self, config: RepoInsightConfig, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.config = config

    async def _run_task(self) -> str | None:
        """Run the documentation generation task."""
        try:
            # Report initial progress
            self.progress.emit(0, "Initializing documentation engine...")

            # Create processing engine
            engine = ProcessingEngine(self.config)

            # Report progress
            self.progress.emit(10, "Scanning repository...")

            # Process repository and generate markdown
            snapshot, markdown = await engine.process_and_generate()

            # Report progress
            self.progress.emit(100, "Documentation generation completed")

            # Return the generated markdown
            return markdown
        except Exception as e:
            logger.exception("Error generating documentation")
            self.error.emit(f"Error generating documentation: {str(e)}")
            return None
