# repoinsight-gemma3-4b Documentation

## Repository Information

### Repository Information

| Property           | Value                                 |
| ------------------ | ------------------------------------- |
| **Path**           | /home/mw/Projects/satware/repoinsight |
| **Git Repository** | Yes                                   |
| **Generated**      | 2025-04-17T15:23:12.346194            |

### Git Information

| Property           | Value                                            |
| ------------------ | ------------------------------------------------ |
| **Branch**         | main                                             |
| **Commit**         | e3bd926ea7818b0cb2927cdf670c33f7969d41f4         |
| **Commit Message** | Update LLM configuration and documentation paths |

Changed the LLM model and API base URL in `.repoinsight.yml` for compatibility with the new provider. Adjusted documentation structure to reflect updates in codebase organization and metadata details. |
| **Commit Date** | 2025-04-16T21:41:33 |
| **Author** | Michael Wegener <mw@satware.com> |

### Remote Repositories

| Property     | Value                                        |
| ------------ | -------------------------------------------- |
| **Remote 1** | https://github.com/satwareAG/repoinsight.git |

## Table of Contents

- [verify_thread_fix.py](#file__home_mw_Projects_satware_repoinsight_verify_thread_fix_py_0)
- [verify_gui_flag.py](#file__home_mw_Projects_satware_repoinsight_verify_gui_flag_py_1)
- [test_gui_flag.py](#file__home_mw_Projects_satware_repoinsight_test_gui_flag_py_2)
- [detailed_test.py](#file__home_mw_Projects_satware_repoinsight_detailed_test_py_3)
- [check_ruff_errors.py](#file__home_mw_Projects_satware_repoinsight_check_ruff_errors_py_4)
- [run_repoinsight.py](#file__home_mw_Projects_satware_repoinsight_run_repoinsight_py_5)
- [INSTALL.md](#file__home_mw_Projects_satware_repoinsight_INSTALL_md_6)
- [test_gui.py](#file__home_mw_Projects_satware_repoinsight_test_gui_py_7)
- [README.md](#file__home_mw_Projects_satware_repoinsight_README_md_8)
  - [src/repoinsight/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight___init___py_9)
  - [src/repoinsight/**main**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight___main___py_10)
    - [src/repoinsight/cli/commands.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_cli_commands_py_11)
    - [src/repoinsight/cli/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_cli___init___py_12)
    - [src/repoinsight/scanner/engine.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_scanner_engine_py_13)
    - [src/repoinsight/scanner/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_scanner___init___py_14)
    - [src/repoinsight/scanner/filters.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_scanner_filters_py_15)
    - [src/repoinsight/core/engine.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_core_engine_py_16)
    - [src/repoinsight/core/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_core___init___py_17)
    - [src/repoinsight/core/models.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_core_models_py_18)
    - [src/repoinsight/markdown/generator.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_markdown_generator_py_19)
    - [src/repoinsight/markdown/components.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_markdown_components_py_20)
    - [src/repoinsight/markdown/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_markdown___init___py_21)
    - [src/repoinsight/config/yaml.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_config_yaml_py_22)
    - [src/repoinsight/config/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_config___init___py_23)
    - [src/repoinsight/config/models.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_config_models_py_24)
    - [src/repoinsight/gui/config_panel.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_config_panel_py_25)
    - [src/repoinsight/gui/worker.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_worker_py_26)
    - [src/repoinsight/gui/preview_panel.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_preview_panel_py_27)
    - [src/repoinsight/gui/profile_panel.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_profile_panel_py_28)
    - [src/repoinsight/gui/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui___init___py_29)
    - [src/repoinsight/gui/app.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_app_py_30)
    - [src/repoinsight/gui/main_window.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_main_window_py_31)
    - [src/repoinsight/llm/client.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm_client_py_32)
    - [src/repoinsight/llm/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm___init___py_33)
    - [src/repoinsight/llm/prompts.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm_prompts_py_34)
    - [src/repoinsight/llm/cache.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm_cache_py_35)
    - [src/repoinsight/git/repository.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_git_repository_py_36)
    - [src/repoinsight/git/**init**.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_git___init___py_37)
    - [src/repoinsight/git/metadata.py](#file__home_mw_Projects_satware_repoinsight_src_repoinsight_git_metadata_py_38)
  - [tests/**init**.py](#file__home_mw_Projects_satware_repoinsight_tests___init___py_39)
  - [tests/test_config.py](#file__home_mw_Projects_satware_repoinsight_tests_test_config_py_40)
  - [.clinerules/04-security.md](#file__home_mw_Projects_satware_repoinsight__clinerules_04-security_md_41)
  - [.clinerules/06-advanced-features.md](#file__home_mw_Projects_satware_repoinsight__clinerules_06-advanced-features_md_42)
  - [.clinerules/02-procject-structure.md](#file__home_mw_Projects_satware_repoinsight__clinerules_02-procject-structure_md_43)
  - [.clinerules/09-cross-agent-collaboration.md](#file__home_mw_Projects_satware_repoinsight__clinerules_09-cross-agent-collaboration_md_44)
  - [.clinerules/07-ui-standards.md](#file__home_mw_Projects_satware_repoinsight__clinerules_07-ui-standards_md_45)
  - [.clinerules/01-tech-stack.md](#file__home_mw_Projects_satware_repoinsight__clinerules_01-tech-stack_md_46)
  - [.clinerules/05-token-management.md](#file__home_mw_Projects_satware_repoinsight__clinerules_05-token-management_md_47)
  - [.clinerules/03-development-workflow.md](#file__home_mw_Projects_satware_repoinsight__clinerules_03-development-workflow_md_48)
  - [.clinerules/08-performance-benchmarks.md](#file__home_mw_Projects_satware_repoinsight__clinerules_08-performance-benchmarks_md_49)
  - [docs/USAGE.md](#file__home_mw_Projects_satware_repoinsight_docs_USAGE_md_50)

<a id="file__home_mw_Projects_satware_repoinsight_verify_thread_fix_py_0"></a>

## File: verify_thread_fix.py

**Language**: python

### Description

This script automates testing the "QThread: Destroyed while thread is still running" fix by launching and interacting with the RepoInsight GUI, simulating a Run button click, and then closing the application.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 5.5 KB                     |
| **Last Modified** | 2025-04-16T20:33:48.909263 |
| **Type**          | py                         |

```python
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

```

<a id="file__home_mw_Projects_satware_repoinsight_verify_gui_flag_py_1"></a>

## File: verify_gui_flag.py

**Language**: python

### Description

This script verifies the `--gui` flag is present in `repoinsight`’s help output and tests invalid flag handling.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.6 KB                     |
| **Last Modified** | 2025-04-16T19:22:17.489996 |
| **Type**          | py                         |

```python
#!/usr/bin/env python
"""
Simple verification script for the --gui flag.
This checks that the flag appears in the help output.
"""

import subprocess
import sys


def run_command(cmd):
    """Run a command and return its output."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode


def main() -> None:
    print("Verifying --gui flag implementation")
    print("=" * 40)

    # Check if --gui appears in help output
    stdout, stderr, code = run_command([sys.executable, "-m", "repoinsight", "--help"])
    print(f"Return code: {code}")

    # Print the full help output for debugging
    print("\nHelp Output:")
    print("-" * 40)
    print(stdout)
    print("-" * 40)

    if "--gui" in stdout:
        print("SUCCESS: --gui flag is mentioned in help output")
        # Find the line containing --gui
        for line in stdout.split("\n"):
            if "--gui" in line:
                print(f"Found in help: {line}")
                break
    else:
        print("ERROR: --gui flag not found in help output")
    print("-" * 40)

    # Try invalid flag to verify error handling
    stdout, stderr, code = run_command([sys.executable, "-m", "repoinsight", "--invalid-flag"])
    print(f"Invalid flag test return code: {code}")
    if code != 0:
        print("SUCCESS: Invalid flag correctly causes error")
    else:
        print("ERROR: Invalid flag didn't cause error")
    print("-" * 40)

    print("Verification complete")


if __name__ == "__main__":
    main()

```

<a id="file__home_mw_Projects_satware_repoinsight_test_gui_flag_py_2"></a>

## File: test_gui_flag.py

**Language**: python

### Description

This script tests the `--gui` flag by mocking the `run_app` function and verifying its execution within the main application logic.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.4 KB                     |
| **Last Modified** | 2025-04-16T19:22:17.489996 |
| **Type**          | py                         |

```python
#!/usr/bin/env python
"""
Test script to verify the --gui flag functionality.
This script simply intercepts the run_app function call to avoid actually launching a window.
"""

import logging
from unittest.mock import patch

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

print("Script started - testing GUI flag implementation")


# Mock the GUI launch to avoid actually opening a window
def mock_run_app() -> int:
    print("SUCCESS: GUI would be launched here!")
    logger.debug("run_app function was called")
    return 0


try:
    # Patch the run_app function in the gui.app module
    with patch("repoinsight.gui.app.run_app", mock_run_app):
        # Import the main function after patching
        print("Importing main function...")
        from repoinsight.__main__ import main

        # Test with --gui flag
        print("Testing with --gui flag...")
        exit_code = main(["--gui"])
        print(f"Exit code: {exit_code}")

        # Test with --gui and additional flags
        print("\nTesting with --gui and additional flags...")
        exit_code = main(["--gui", "--verbose"])
        print(f"Exit code: {exit_code}")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback

    traceback.print_exc()

print("Script finished")

```

<a id="file__home_mw_Projects_satware_repoinsight_detailed_test_py_3"></a>

## File: detailed_test.py

**Language**: python

### Description

This script thoroughly tests the `--gui` flag by instrumenting a CLI application to track GUI launches and command arguments.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 3.9 KB                     |
| **Last Modified** | 2025-04-16T19:04:26.824106 |
| **Type**          | py                         |

```python
#!/usr/bin/env python
"""
Detailed test script for the --gui flag.
This creates a test harness that intercepts several functions to track exactly what's happening.
"""

import logging
import sys
from unittest.mock import MagicMock, patch

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create mock objects for tracking function calls
mock_run_app = MagicMock(return_value=0)
mock_run_app.__name__ = "run_app"  # needed for some decorators

# List to capture command line args as they're processed
captured_args = []


def args_capturer(*args, **kwargs):
    """Capture arguments being passed to typer callback"""
    logger.debug(f"Callback called with: args={args}, kwargs={kwargs}")
    captured_args.append((args, kwargs))
    # Continue with original function
    return original_main(*args, **kwargs)


print("=" * 60)
print("Starting detailed GUI flag test")
print("=" * 60)

try:
    # Step 1: Patch gui.app.run_app to prevent actual GUI from launching
    with patch("repoinsight.gui.app.run_app", mock_run_app):
        # Get a reference to the CLI commands module
        from repoinsight.cli import commands

        # Step 2: Store reference to original main callback function
        original_main = commands.main

        # Step 3: Replace the main callback with our instrumented version
        commands.main = args_capturer

        # Test various command combinations
        test_cases = [
            ["--gui"],
            ["--gui", "--help"],
            ["run", "--help"],
            ["--version", "--gui"],
            ["--gui", "run", "--repository", "."],
        ]

        for i, args in enumerate(test_cases):
            print(f"\nTest case {i+1}: {' '.join(args)}")
            print("-" * 40)

            # Reset state for this test
            captured_args.clear()
            mock_run_app.reset_mock()

            # Import main module fresh to avoid state from previous tests
            if "repoinsight.__main__" in sys.modules:
                del sys.modules["repoinsight.__main__"]

            # Run the main function with our test arguments
            from repoinsight.__main__ import main

            try:
                exit_code = main(args)
                print(f"Exit code: {exit_code}")
            except SystemExit as e:
                print(f"SystemExit with code: {e.code}")
            except Exception as e:
                print(f"Exception: {type(e).__name__}: {e}")

            # Check if GUI was launched
            if mock_run_app.called:
                print("✓ GUI was launched")
                print(f"  Times called: {mock_run_app.call_count}")
            else:
                print("✗ GUI was NOT launched")

            # Print captured args if any
            if captured_args:
                print("Callback args captured:")
                for args_tuple in captured_args:
                    print(f"  - Args: {args_tuple[0]}, Kwargs: {args_tuple[1]}")

            print("-" * 40)

    print("\nFinal verification:")
    print("=" * 40)
    # Reset all our patches and mocks
    commands.main = original_main

    # Try direct test with our verification harness
    with patch("repoinsight.gui.app.run_app") as final_mock:
        final_mock.return_value = 0
        final_mock.__name__ = "run_app"

        print("Running final test: 'python -m repoinsight --gui'")
        if "repoinsight.__main__" in sys.modules:
            del sys.modules["repoinsight.__main__"]

        from repoinsight.__main__ import main

        exit_code = main(["--gui"])

        if final_mock.called:
            print("TEST PASSED: --gui flag properly calls the GUI application")
        else:
            print("TEST FAILED: --gui flag did not launch the GUI application")

except Exception as e:
    import traceback

    print(f"Test framework error: {e}")
    traceback.print_exc()

print("\nDetailed test complete")
print("=" * 60)

```

<a id="file__home_mw_Projects_satware_repoinsight_check_ruff_errors_py_4"></a>

## File: check_ruff_errors.py

**Language**: python

### Description

This script verifies the B008 linting configuration by running ruff on a specified file and reporting the results.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.0 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.388706 |
| **Type**          | py                         |

```python
"""
Simple script to check if our configuration for B008 is working properly.
"""
import os
import sys
from pathlib import Path

# Use direct module imports for more reliable execution
try:
    from ruff.__main__ import find_ruff_bin

    ruff_path = find_ruff_bin()
except ImportError:
    print("Could not import ruff module. Make sure it's installed.")
    sys.exit(1)

# Path to the file to check
commands_path = Path("src/repoinsight/cli/commands.py").absolute()

if not commands_path.exists():
    print(f"File not found: {commands_path}")
    sys.exit(1)

print(f"Using ruff at: {ruff_path}")
print(f"Checking file: {commands_path}")
print(f"Current directory: {os.getcwd()}")
print("\nChecking for B008 errors...\n")

# Execute ruff directly
result = os.system(f"{ruff_path} check --select=B008 {commands_path}")

# Explain the result
if result == 0:
    print("\nSuccess! No B008 errors found. The configuration is working correctly.")
else:
    print("\nB008 errors still exist. The configuration may need adjustment.")

sys.exit(0 if result == 0 else 1)

```

<a id="file__home_mw_Projects_satware_repoinsight_run_repoinsight_py_5"></a>

## File: run_repoinsight.py

**Language**: python

### Description

This script programmatically runs RepoInsight to process a repository and generate markdown documentation.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.9 KB                     |
| **Last Modified** | 2025-04-16T17:45:20.197173 |
| **Type**          | py                         |

```python
#!/usr/bin/env python
"""
Example script for running RepoInsight.

This script demonstrates how to run RepoInsight programmatically.
"""

import asyncio
import logging
import sys
from pathlib import Path

from repoinsight.config.yaml import load_config
from repoinsight.core.engine import ProcessingEngine


async def main() -> int:
    """Run RepoInsight programmatically."""
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    try:
        # Load configuration from sample file
        config_path = Path("sample_config.yml")
        if not config_path.exists():
            print(f"Error: Configuration file not found: {config_path}")
            return 1

        config = load_config(config_path)
        print(f"Loaded configuration: {config.name}")

        # Create processing engine
        engine = ProcessingEngine(config)

        # Process repository and generate markdown
        print("Processing repository...")
        snapshot, markdown = await engine.process_and_generate()

        # Print some stats
        print(f"Processed {len(snapshot.files)} files")

        # Save output if path is specified
        if config.output_path:
            output_path = config.get_absolute_output_path()
            if output_path:
                print(f"Documentation saved to: {output_path}")
            else:
                print("No output path specified")
        else:
            # Print a preview of the markdown
            print("\nMarkdown Preview (first 500 characters):")
            print("-" * 80)
            print(markdown[:500] + "...")
            print("-" * 80)

        return 0
    except Exception as e:
        print(f"Error: {e}")
        logging.exception("Error running RepoInsight")
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

```

<a id="file__home_mw_Projects_satware_repoinsight_INSTALL_md_6"></a>

## File: INSTALL.md

**Language**: markdown

### Description

This guide details how to install and set up RepoInsight, a repository analysis tool, using either Poetry or pip.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 3.1 KB                     |
| **Last Modified** | 2025-04-16T17:52:01.127614 |
| **Type**          | md                         |

````markdown
# Installation Guide for satware® RepoInsight

This guide provides detailed instructions for installing and setting up RepoInsight on different platforms.

## Prerequisites

- Python 3.11, 3.12, or 3.13
- Git (for repository analysis)
- Cortex or another OpenAI-compatible LLM server (optional, for AI-generated descriptions)

## Option 1: Installation with Poetry (Recommended)

[Poetry](https://python-poetry.org/) is the recommended dependency management tool for RepoInsight.

### 1. Install Poetry

#### Linux/macOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
````

#### Windows

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 2. Clone the Repository

```bash
git clone https://github.com/satware/repoinsight.git
cd repoinsight
```

### 3. Install Dependencies

```bash
poetry install
```

### 4. Run RepoInsight

```bash
# CLI mode
poetry run repoinsight

# GUI mode
poetry run repoinsight --gui
```

## Option 2: Installation with pip

### 1. Clone the Repository

```bash
git clone https://github.com/satware/repoinsight.git
cd repoinsight
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install RepoInsight in Development Mode

```bash
pip install -e .
```

### 5. Run RepoInsight

```bash
# CLI mode
python -m repoinsight

# GUI mode
python -m repoinsight --gui
```

## Setting Up Cortex for LLM Integration

RepoInsight can use Cortex or other OpenAI-compatible LLM servers to generate descriptions of source code files.

### Running Cortex Locally

1. Install Cortex by following the instructions at <https://cortex.so/docs>

2. Start the Cortex server:

```bash
cortex run llama3
```

3. Configure RepoInsight to use Cortex:
   - Edit your configuration file (e.g., `sample_config.yml`)
   - Ensure `llm.enabled` is set to `true`
   - Set `llm.api_base_url` to your Cortex server URL (default: `http://localhost:8000/v1`)
   - Set `llm.model` to the model you're running (e.g., `llama3`)

## Common Issues and Troubleshooting

### Qt/PySide6 Installation Issues

If you encounter issues installing PySide6, you may need to install additional system dependencies:

#### Ubuntu/Debian

```bash
sudo apt-get install libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xkb1 libxkbcommon-x11-0
```

#### Fedora/RHEL

```bash
sudo dnf install libxcb libxkbcommon-x11
```

#### macOS

```bash
brew install cmake
```

### LLM Integration Issues

If you're having trouble connecting to your LLM server:

1. Verify the server is running and accessible
2. Check your API URL configuration
3. If using Cortex, ensure the model is loaded correctly
4. Try increasing the timeout value in your configuration

## Installing Pre-commit Hooks (for Developers)

```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install
```

````


<a id="file__home_mw_Projects_satware_repoinsight_test_gui_py_7"></a>

## File: test_gui.py

**Language**: python

### Description

This script launches the RepoInsight GUI for testing and demonstration purposes.<end_of_turn>

### Metadata

| Property | Value |
| --- | --- |
| **Size** | 436 bytes |
| **Last Modified** | 2025-04-16T19:04:26.824677 |
| **Type** | py |



```python
#!/usr/bin/env python
"""
Test script for running the RepoInsight GUI.

This script demonstrates how to run the RepoInsight GUI directly.
"""

import logging
import sys

from repoinsight.gui import run_app

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Run the application
    sys.exit(run_app())

````

<a id="file__home_mw_Projects_satware_repoinsight_README_md_8"></a>

## File: README.md

**Language**: markdown

### Description

RepoInsight automatically generates richly annotated markdown documentation for Git repositories, optionally enhanced with AI-powered descriptions.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 3.0 KB                     |
| **Last Modified** | 2025-04-16T16:47:35.042836 |
| **Type**          | md                         |

````markdown
# satware® RepoInsight

A powerful cross-platform application for automatic documentation of Git repositories with AI-enhanced descriptions.

## Overview

satware® RepoInsight automatically aggregates source code files from any Git repository (or folder structure), combines them into a richly annotated, single markdown document, and enhances this artifact with AI-generated descriptions using an OpenAI-compatible language model API such as Cortex.

## Features

- **Broad Compatibility**: Support for any Git-hosted or local repository; direct folder processing for repos without version control.
- **YAML-Driven Configurability**: Flexible, human-readable configuration format to specify project roots, file inclusion/exclusion rules, output layout, and AI integration parameters.
- **AI-Powered Summarization**: Seamless integration with Cortex or other OpenAI-compatible LLM servers to generate concise, contextually relevant descriptions per file.
- **Rich Metadata Capture**: Embedding of detailed Git repository metadata, including commit hashes, branch names, remote URLs, and generation timestamps.
- **Robust File Scanning**: Efficient, recursive discovery of source files using filters and exclusion rules; accurate language detection for markdown syntax highlighting.
- **Markdown Generation**: Creation of clean, CommonMark-compliant markdown documents with auto-generated Table of Contents, per-file sections, and metadata tags.
- **Cross-Platform GUI**: Modern, intuitive interface built on PySide6, optimized for Linux, Windows, and macOS.
- **Efficient Caching**: Local, filesystem-based caching keyed by file path and repository commit to ensure minimal redundant API calls.

## Installation

### Prerequisites

- Python 3.11 or newer
- Git (for repository analysis)
- Cortex or another OpenAI-compatible LLM server (optional, for AI-generated descriptions)

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/satware/repoinsight.git
cd repoinsight

# Install dependencies with Poetry
poetry install

# Run the application
poetry run repoinsight
```
````

### Using pip

```bash
# Install from PyPI
pip install repoinsight

# Run the application
repoinsight
```

## Quick Start

1. Launch the application
2. Select a Git repository or folder
3. Configure file inclusion/exclusion patterns
4. Set up LLM integration (optional)
5. Generate the documentation
6. View and export the markdown document

## Configuration

RepoInsight uses YAML configuration files to customize its behavior. Here's a basic example:

```yaml
name: "My Project Documentation"
root_path: "/path/to/repository"
scan_directories:
  - "src"
  - "docs"
exclude_directories:
  - "venv"
  - "node_modules"
  - ".git"
file_patterns:
  include:
    - "*.py"
    - "*.js"
    - "*.md"
  exclude:
    - "*.pyc"
    - "*.min.js"
llm:
  enabled: true
  api_base_url: "http://localhost:8000/v1"
  model: "llama3"
  temperature: 0.3
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

````


<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight___init___py_9"></a>

## File: src/repoinsight/__init__.py

**Language**: python

### Description

This code generates automated Git repository documentation using AI for enhanced descriptions.<end_of_turn>

### Metadata

| Property | Value |
| --- | --- |
| **Size** | 168 bytes |
| **Last Modified** | 2025-04-16T16:47:53.116049 |
| **Type** | py |



```python
"""
satware® RepoInsight - Automated Git repository documentation with AI-enhanced descriptions.
"""

__version__ = "0.1.0"
__author__ = "satware"
__license__ = "MIT"

````

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight___main___py_10"></a>

## File: src/repoinsight/**main**.py

**Language**: python

### Description

This Python code serves as the main application entry point, launching either the command-line interface or GUI for RepoInsight.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 726 bytes                  |
| **Last Modified** | 2025-04-16T17:39:13.785001 |
| **Type**          | py                         |

```python
"""
Main entry point for RepoInsight.

This module provides the main entry point for the application,
allowing users to choose between the CLI and GUI interfaces.
"""

import logging
import sys

from repoinsight.cli.commands import app as cli_app


def main(args: list[str] | None = None) -> int:
    """
    Main entry point for the application.

    Args:
        args: Command-line arguments

    Returns:
        Exit code
    """
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Run the CLI app (which now handles the --gui flag internally)
    return cli_app()


if __name__ == "__main__":
    sys.exit(main())

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_cli_commands_py_11"></a>

## File: src/repoinsight/cli/commands.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 14.7 KB                    |
| **Last Modified** | 2025-04-16T19:15:29.654870 |
| **Type**          | py                         |

```python
"""
Command-line interface commands for RepoInsight.

This module defines the command-line interface using Typer.
"""

import asyncio
import logging
import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress, SpinnerColumn, TextColumn

from repoinsight import __version__
from repoinsight.config.models import RepoInsightConfig
from repoinsight.config.yaml import ConfigManager, find_config_file, load_config
from repoinsight.core.engine import ProcessingEngine
from repoinsight.gui.app import run_app

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, markup=True)],
)
logger = logging.getLogger("repoinsight")

# Create the console for rich output
console = Console()

# Create the Typer app
app = typer.Typer(
    help="RepoInsight: Automated documentation for Git repositories with AI-enhanced descriptions",
    add_completion=False,
)

# Create subcommands
config_app = typer.Typer(help="Manage configuration profiles")
app.add_typer(config_app, name="config")

cache_app = typer.Typer(help="Manage LLM cache")
app.add_typer(cache_app, name="cache")


@app.command("version")
def version() -> None:
    """
    Show the version of RepoInsight.
    """
    console.print(f"RepoInsight v{__version__}")


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    gui: bool = typer.Option(
        False,
        "--gui",
        help="Launch the graphical user interface",
    ),
) -> None:
    """
    Main callback for RepoInsight CLI.

    This function runs before any command and can intercept to launch the GUI.
    """
    if gui:
        # If --gui flag is used, launch the GUI and exit
        sys.exit(run_app())

    # If no command is provided and --gui is not used, show help
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        sys.exit(0)


@app.command("run")
def run(
    config_file: Path | None = typer.Option(
        None,
        "--config",
        "-c",
        help="Path to configuration file",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
    ),
    profile: str | None = typer.Option(
        None,
        "--profile",
        "-p",
        help="Configuration profile to use",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output path for the generated documentation",
        file_okay=True,
        dir_okay=False,
        writable=True,
    ),
    repository: Path | None = typer.Option(
        None,
        "--repository",
        "-r",
        help="Path to repository (overrides configuration)",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
    ),
) -> None:
    """
    Run RepoInsight to generate documentation.
    """
    try:
        # Load configuration
        config = _load_configuration(config_file, profile)

        # Override with command-line options
        if repository:
            config.root_path = str(repository.absolute())
            console.print(f"Using repository: [bold]{config.root_path}[/bold]")

        if output:
            config.output_path = str(output.absolute())
            console.print(f"Using output path: [bold]{config.output_path}[/bold]")

        # Run the processing engine
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            # Create a task for the main progress
            task = progress.add_task("Processing repository...", total=None)

            # Run the engine
            asyncio.run(_run_engine(config, progress, task))

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("Error running RepoInsight")
        sys.exit(1)


async def _run_engine(config: RepoInsightConfig, progress: Progress, task_id: int) -> None:
    """
    Run the processing engine asynchronously.

    Args:
        config: Configuration to use
        progress: Progress object for displaying progress
        task_id: Task ID for updating progress
    """
    # Create the processing engine
    engine = ProcessingEngine(config)

    # Process repository
    progress.update(task_id, description="Scanning repository...")
    snapshot = await engine.process_repository()

    # Generate markdown
    progress.update(task_id, description="Generating markdown...")
    markdown = await engine.generate_markdown(snapshot)

    # Save output if path is specified
    if config.output_path:
        output_path = config.get_absolute_output_path()
        if output_path:
            # Ensure directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Write markdown to file
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown)

            progress.update(task_id, description=f"Saved to {output_path}")
            progress.remove_task(task_id)

            console.print(f"Documentation generated and saved to: [bold]{output_path}[/bold]")

    else:
        # No output path specified, print to console
        progress.remove_task(task_id)
        console.print("\nGenerated Documentation:\n")
        console.print(markdown)


@app.command("init")
def init(
    path: Path | None = typer.Argument(
        None,
        help="Path to initialize configuration",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        writable=True,
    ),
    name: str | None = typer.Option(
        None,
        "--name",
        "-n",
        help="Name for the configuration",
    ),
) -> None:
    """
    Initialize a new configuration file.
    """
    try:
        # Use current directory if not specified
        if not path:
            path = Path.cwd()

        # Use directory name as configuration name if not specified
        if not name:
            name = path.name

        # Create configuration
        config = RepoInsightConfig(
            name=name,
            root_path=str(path.absolute()),
        )

        # Save configuration
        config_path = path / ".repoinsight.yml"
        if config_path.exists():
            msg = f"Configuration file already exists at {config_path}. Overwrite?"
            confirm = typer.confirm(msg)
            if not confirm:
                console.print("Cancelled.")
                return

        # Convert config to dictionary and save as YAML
        from repoinsight.config.yaml import save_config

        save_config(config, config_path)

        console.print(f"Configuration initialized at: [bold]{config_path}[/bold]")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("Error initializing configuration")
        sys.exit(1)


@config_app.command("list")
def list_profiles() -> None:
    """
    List available configuration profiles.
    """
    try:
        # Get the configuration manager
        config_manager = ConfigManager()

        # Get available profiles
        profiles = config_manager.get_available_profiles()

        if profiles:
            console.print("Available configuration profiles:")
            for profile in profiles:
                console.print(f"  - [bold]{profile}[/bold]")
        else:
            console.print("No configuration profiles found.")
            console.print(f"Profiles directory: [dim]{config_manager.profiles_dir}[/dim]")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("Error listing profiles")
        sys.exit(1)


@config_app.command("create")
def create_profile(
    name: str = typer.Argument(..., help="Name for the profile"),
    repository: Path | None = typer.Option(
        None,
        "--repository",
        "-r",
        help="Path to repository",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
    ),
) -> None:
    """
    Create a new configuration profile.
    """
    try:
        # Get the configuration manager
        config_manager = ConfigManager()

        # Check if profile already exists
        profiles = config_manager.get_available_profiles()
        if name in profiles:
            confirm = typer.confirm(f"Profile '{name}' already exists. Overwrite?")
            if not confirm:
                console.print("Cancelled.")
                return

        # Use current directory if repository not specified
        if not repository:
            repository = Path.cwd()

        # Create configuration
        config = RepoInsightConfig(
            name=name,
            root_path=str(repository.absolute()),
        )

        # Save profile
        config_manager.save_profile(config, name)

        console.print(f"Profile [bold]{name}[/bold] created.")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("Error creating profile")
        sys.exit(1)


@config_app.command("delete")
def delete_profile(
    name: str = typer.Argument(..., help="Name of the profile to delete"),
) -> None:
    """
    Delete a configuration profile.
    """
    try:
        # Get the configuration manager
        config_manager = ConfigManager()

        # Check if profile exists
        profiles = config_manager.get_available_profiles()
        if name not in profiles:
            console.print(f"Profile [bold]{name}[/bold] does not exist.")
            return

        # Confirm deletion
        confirm = typer.confirm(f"Are you sure you want to delete profile '{name}'?")
        if not confirm:
            console.print("Cancelled.")
            return

        # Delete profile
        if config_manager.delete_profile(name):
            console.print(f"Profile [bold]{name}[/bold] deleted.")
        else:
            console.print(f"Failed to delete profile [bold]{name}[/bold].")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("Error deleting profile")
        sys.exit(1)


@cache_app.command("info")
def cache_info() -> None:
    """
    Show information about the LLM cache.
    """
    try:
        # Get the configuration manager
        config_manager = ConfigManager()

        # Load default configuration
        config = config_manager.load_default_config()

        # Get cache directory
        cache_dir = config.get_absolute_cache_path()

        # Print information
        console.print(f"Cache directory: [bold]{cache_dir}[/bold]")

        if not cache_dir.exists():
            console.print("Cache directory does not exist.")
            return

        # Count files and total size
        file_count = 0
        total_size = 0

        for cache_file in cache_dir.glob("*.json"):
            file_count += 1
            total_size += cache_file.stat().st_size

        console.print(f"Files: [bold]{file_count}[/bold]")
        console.print(f"Total size: [bold]{_format_size(total_size)}[/bold]")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("Error getting cache info")
        sys.exit(1)


@cache_app.command("clear")
def clear_cache(
    older_than: int | None = typer.Option(
        None,
        "--older-than",
        "-o",
        help="Clear only entries older than this many days",
    ),
) -> None:
    """
    Clear the LLM cache.
    """
    try:
        # Get the configuration manager
        config_manager = ConfigManager()

        # Load default configuration
        config = config_manager.load_default_config()

        # Get cache directory
        cache_dir = config.get_absolute_cache_path()

        if not cache_dir.exists():
            console.print("Cache directory does not exist.")
            return

        # Confirm deletion
        if older_than:
            confirm = typer.confirm(f"Clear cache entries older than {older_than} days?")
        else:
            confirm = typer.confirm("Clear all cache entries?")

        if not confirm:
            console.print("Cancelled.")
            return

        # Clear cache
        count = 0

        if older_than:
            # Convert days to seconds
            older_than_seconds = older_than * 24 * 60 * 60

            import time

            now = time.time()

            for cache_file in cache_dir.glob("*.json"):
                if now - cache_file.stat().st_mtime > older_than_seconds:
                    cache_file.unlink()
                    count += 1
        else:
            # Clear all cache entries
            for cache_file in cache_dir.glob("*.json"):
                cache_file.unlink()
                count += 1

        console.print(f"Cleared [bold]{count}[/bold] cache entries.")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("Error clearing cache")
        sys.exit(1)


def _load_configuration(config_file: Path | None, profile: str | None) -> RepoInsightConfig:
    """
    Load the configuration from a file or profile.

    Args:
        config_file: Path to configuration file
        profile: Configuration profile name

    Returns:
        Loaded configuration
    """
    # Create the configuration manager
    config_manager = ConfigManager()

    # Try each possible configuration source in order

    # 1. Try to load from specified profile
    if profile:
        try:
            return config_manager.load_profile(profile)
        except FileNotFoundError:
            console.print(f"[yellow]Profile '{profile}' not found.[/yellow]")

    # 2. Try to load from specified configuration file
    if config_file:
        try:
            return load_config(config_file)
        except Exception as e:
            console.print(f"[yellow]Failed to load configuration file: {e}[/yellow]")

    # 3. Try to find a configuration file in the current directory
    found_config = find_config_file()
    if found_config:
        try:
            return load_config(found_config)
        except Exception as e:
            console.print(f"[yellow]Failed to load found configuration file: {e}[/yellow]")

    # 4. Fallback to default configuration with current directory
    console.print("[yellow]Using default configuration.[/yellow]")
    return config_manager.load_default_config()


def _format_size(size_bytes: int) -> str:
    """Format file size in a human-readable way."""
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    if size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"


if __name__ == "__main__":
    app()

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_cli___init___py_12"></a>

## File: src/repoinsight/cli/**init**.py

**Language**: python

### Description

This Python code defines a command-line interface package for RepoInsight, exposing its core functionality through the `app` module.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 188 bytes                  |
| **Last Modified** | 2025-04-16T16:58:01.857816 |
| **Type**          | py                         |

```python
"""
Command-line interface package for RepoInsight.

This package provides the command-line interface for the application.
"""

from repoinsight.cli.commands import app

__all__ = ["app"]

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_scanner_engine_py_13"></a>

## File: src/repoinsight/scanner/engine.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 7.8 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.389077 |
| **Type**          | py                         |

```python
"""
File scanning engine for RepoInsight.

This module provides functionality for scanning repositories and directories
to discover files for documentation.
"""

import asyncio
import fnmatch
import os
from pathlib import Path

from repoinsight.config.models import FilePatterns


class RepositoryScanner:
    """
    Scanner for discovering and filtering files in a repository.
    """

    def __init__(
        self,
        root_path: str | Path,
        file_patterns: FilePatterns | None = None,
        exclude_dirs: list[str] | None = None,
        scan_dirs: list[str] | None = None,
    ) -> None:
        """
        Initialize a repository scanner.

        Args:
            root_path: Root path of the repository to scan
            file_patterns: Patterns for including/excluding files
            exclude_dirs: Directories to exclude from scanning
            scan_dirs: Directories to scan (relative to root_path)
        """
        self.root_path = Path(root_path)
        self.file_patterns = file_patterns or FilePatterns()
        self.exclude_dirs = set(exclude_dirs or ["venv", "node_modules", ".git"])
        self.scan_dirs = scan_dirs or ["."]

    def is_excluded_dir(self, dir_path: Path) -> bool:
        """
        Check if a directory should be excluded from scanning.

        Args:
            dir_path: Path to the directory

        Returns:
            True if the directory should be excluded, False otherwise
        """
        # Convert to relative path if it's absolute
        if dir_path.is_absolute():
            try:
                # Get relative path from root
                rel_path = dir_path.relative_to(self.root_path)
                dir_path = rel_path
            except ValueError:
                # Path is not relative to root, shouldn't happen
                return True

        dir_str = str(dir_path)

        # Check if any part of the path matches an excluded directory
        path_parts = dir_path.parts
        for part in path_parts:
            if part in self.exclude_dirs:
                return True

        # Check patterns
        return any(fnmatch.fnmatch(dir_str, pattern) for pattern in self.exclude_dirs)

    def is_included_file(self, file_path: Path) -> bool:
        """
        Check if a file should be included based on patterns.

        Args:
            file_path: Path to the file

        Returns:
            True if the file should be included, False otherwise
        """
        # Convert to relative path if it's absolute
        if file_path.is_absolute():
            try:
                # Get relative path from root
                rel_path = file_path.relative_to(self.root_path)
                file_path = rel_path
            except ValueError:
                # Path is not relative to root, shouldn't happen
                return False

        file_str = str(file_path)

        # First check exclusion patterns
        for pattern in self.file_patterns.exclude:
            if fnmatch.fnmatch(file_str, pattern):
                return False

        # Then check inclusion patterns
        return any(fnmatch.fnmatch(file_str, pattern) for pattern in self.file_patterns.include)

    def scan(self) -> list[Path]:
        """
        Scan the repository for files.

        Returns:
            List of file paths that match the inclusion/exclusion patterns
        """
        included_files = []

        for scan_dir in self.scan_dirs:
            scan_path = self.root_path / scan_dir
            if not scan_path.exists():
                continue

            # Walk the directory tree
            for root, dirs, files in os.walk(scan_path):
                root_path = Path(root)

                # Filter out excluded directories (modify dirs in-place to avoid walking them)
                dirs[:] = [d for d in dirs if not self.is_excluded_dir(root_path / d)]

                # Filter and add files
                for file in files:
                    file_path = root_path / file
                    if self.is_included_file(file_path):
                        included_files.append(file_path)

        return included_files

    async def scan_async(self) -> list[Path]:
        """
        Scan the repository asynchronously.

        This method is a coroutine wrapper around the synchronous scan method,
        but runs the scan in a separate thread to avoid blocking the event loop.

        Returns:
            List of file paths that match the inclusion/exclusion patterns
        """
        # Run the synchronous scan in a separate thread
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, self.scan)


class FileTypeDetector:
    """
    Detector for file types and languages.
    """

    # Mapping of file extensions to languages
    EXTENSION_TO_LANGUAGE = {
        # Common programming languages
        "py": "python",
        "js": "javascript",
        "jsx": "javascript",
        "ts": "typescript",
        "tsx": "typescript",
        "html": "html",
        "css": "css",
        "scss": "scss",
        "less": "less",
        "json": "json",
        "md": "markdown",
        "markdown": "markdown",
        "xml": "xml",
        "yaml": "yaml",
        "yml": "yaml",
        "toml": "toml",
        "ini": "ini",
        "cfg": "ini",
        "conf": "ini",
        "sh": "bash",
        "bash": "bash",
        "bat": "batch",
        "cmd": "batch",
        "ps1": "powershell",
        "java": "java",
        "c": "c",
        "h": "c",
        "cpp": "cpp",
        "hpp": "cpp",
        "cc": "cpp",
        "hh": "cpp",
        "cs": "csharp",
        "rb": "ruby",
        "php": "php",
        "go": "go",
        "rs": "rust",
        "swift": "swift",
        "kt": "kotlin",
        "scala": "scala",
        "dart": "dart",
        "sql": "sql",
        "r": "r",
        "pl": "perl",
        "pm": "perl",
        "lua": "lua",
        "ex": "elixir",
        "exs": "elixir",
        "hs": "haskell",
        "fs": "fsharp",
        "fsx": "fsharp",
        "clj": "clojure",
        "cljs": "clojure",
        "groovy": "groovy",
        "jl": "julia",
        "m": "matlab",
        "mm": "objectivec",
        "coffee": "coffeescript",
        "elm": "elm",
        "erl": "erlang",
        "vue": "vue",
        "svelte": "svelte",
        # Document formats
        "txt": "text",
        "rst": "restructuredtext",
        "pdf": "pdf",
        "doc": "word",
        "docx": "word",
        "xls": "excel",
        "xlsx": "excel",
        "ppt": "powerpoint",
        "pptx": "powerpoint",
        # Configuration formats
        "dockerfile": "dockerfile",
        "jenkinsfile": "jenkinsfile",
        "makefile": "makefile",
        # Other formats
        "svg": "svg",
        "graphql": "graphql",
        "proto": "protobuf",
    }

    @classmethod
    def detect_language(cls, file_path: str | Path) -> str:
        """
        Detect the programming language of a file.

        Args:
            file_path: Path to the file

        Returns:
            Language identifier string, or "unknown" if the language cannot be determined
        """
        path = Path(file_path)

        # Get the file extension (lowercase, without the dot)
        extension = path.suffix.lower().lstrip(".")

        # Special case for files without extension
        if not extension:
            # Check if the filename itself is a known language identifier
            filename = path.name.lower()
            if filename in cls.EXTENSION_TO_LANGUAGE:
                return cls.EXTENSION_TO_LANGUAGE[filename]

            # Some special cases
            special_cases = {
                "dockerfile": "dockerfile",
                "makefile": "makefile",
                "jenkinsfile": "jenkinsfile",
            }

            return special_cases.get(filename, "text")

        # Look up the language by extension
        return cls.EXTENSION_TO_LANGUAGE.get(extension, "unknown")

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_scanner___init___py_14"></a>

## File: src/repoinsight/scanner/**init**.py

**Language**: python

### Description

This Python package facilitates scanning repositories to identify and filter files based on various criteria.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 714 bytes                  |
| **Last Modified** | 2025-04-16T16:51:42.630849 |
| **Type**          | py                         |

```python
"""
File scanning package for RepoInsight.

This package provides functionality for scanning repositories and directories
to discover and filter files for documentation.
"""

from repoinsight.scanner.engine import FileTypeDetector, RepositoryScanner
from repoinsight.scanner.filters import (
    AndFilter,
    ContentFilter,
    FileFilter,
    FilterBuilder,
    LambdaFilter,
    NotFilter,
    OrFilter,
    PatternFilter,
    RegexFilter,
    SizeFilter,
)

__all__ = [
    "RepositoryScanner",
    "FileTypeDetector",
    "FileFilter",
    "AndFilter",
    "OrFilter",
    "NotFilter",
    "PatternFilter",
    "RegexFilter",
    "SizeFilter",
    "ContentFilter",
    "LambdaFilter",
    "FilterBuilder",
]

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_scanner_filters_py_15"></a>

## File: src/repoinsight/scanner/filters.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 8.3 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.389219 |
| **Type**          | py                         |

```python
"""
File filtering utilities for RepoInsight.

This module provides functionality for filtering files based on various criteria
such as patterns, file size, and content.
"""

import fnmatch
import re
from collections.abc import Callable
from pathlib import Path
from re import Pattern

from repoinsight.config.models import FilePatterns


class FileFilter:
    """
    Base class for file filters.

    Filters can be combined using boolean operators (and, or, not).
    """

    def matches(self, file_path: Path) -> bool:
        """
        Check if a file matches the filter criteria.

        Args:
            file_path: Path to the file to check

        Returns:
            True if the file matches, False otherwise
        """
        raise NotImplementedError("Subclasses must implement matches()")

    def __and__(self, other: "FileFilter") -> "AndFilter":
        """Combine with another filter using AND logic."""
        return AndFilter(self, other)

    def __or__(self, other: "FileFilter") -> "OrFilter":
        """Combine with another filter using OR logic."""
        return OrFilter(self, other)

    def __invert__(self) -> "NotFilter":
        """Negate the filter."""
        return NotFilter(self)


class AndFilter(FileFilter):
    """Filter that requires both sub-filters to match."""

    def __init__(self, filter1: FileFilter, filter2: FileFilter) -> None:
        self.filter1 = filter1
        self.filter2 = filter2

    def matches(self, file_path: Path) -> bool:
        return self.filter1.matches(file_path) and self.filter2.matches(file_path)


class OrFilter(FileFilter):
    """Filter that requires at least one sub-filter to match."""

    def __init__(self, filter1: FileFilter, filter2: FileFilter) -> None:
        self.filter1 = filter1
        self.filter2 = filter2

    def matches(self, file_path: Path) -> bool:
        return self.filter1.matches(file_path) or self.filter2.matches(file_path)


class NotFilter(FileFilter):
    """Filter that negates another filter."""

    def __init__(self, base_filter: FileFilter) -> None:
        self.base_filter = base_filter

    def matches(self, file_path: Path) -> bool:
        return not self.base_filter.matches(file_path)


class PatternFilter(FileFilter):
    """Filter that matches files based on glob patterns."""

    def __init__(self, patterns: FilePatterns) -> None:
        self.patterns = patterns

    def matches(self, file_path: Path) -> bool:
        file_str = str(file_path)

        # Check exclusion patterns first
        for pattern in self.patterns.exclude:
            if fnmatch.fnmatch(file_str, pattern):
                return False

        # Then check inclusion patterns
        return any(fnmatch.fnmatch(file_str, pattern) for pattern in self.patterns.include)


class RegexFilter(FileFilter):
    """Filter that matches files based on regular expressions."""

    def __init__(
        self,
        include_patterns: list[str | Pattern] | None = None,
        exclude_patterns: list[str | Pattern] | None = None,
    ) -> None:
        self.include_patterns = []
        self.exclude_patterns = []

        # Compile include patterns
        if include_patterns:
            for pattern in include_patterns:
                if isinstance(pattern, str):
                    self.include_patterns.append(re.compile(pattern))
                else:
                    self.include_patterns.append(pattern)

        # Compile exclude patterns
        if exclude_patterns:
            for pattern in exclude_patterns:
                if isinstance(pattern, str):
                    self.exclude_patterns.append(re.compile(pattern))
                else:
                    self.exclude_patterns.append(pattern)

    def matches(self, file_path: Path) -> bool:
        file_str = str(file_path)

        # Check exclusion patterns first
        for pattern in self.exclude_patterns:
            if pattern.search(file_str):
                return False

        # If no include patterns, include everything not excluded
        if not self.include_patterns:
            return True

        # Check inclusion patterns
        return any(pattern.search(file_str) for pattern in self.include_patterns)


class SizeFilter(FileFilter):
    """Filter that matches files based on size."""

    def __init__(self, min_size: int | None = None, max_size: int | None = None) -> None:
        """
        Initialize a size filter.

        Args:
            min_size: Minimum file size in bytes (inclusive), or None for no minimum
            max_size: Maximum file size in bytes (inclusive), or None for no maximum
        """
        self.min_size = min_size
        self.max_size = max_size

    def matches(self, file_path: Path) -> bool:
        if not file_path.is_file():
            return False

        size = file_path.stat().st_size

        if self.min_size is not None and size < self.min_size:
            return False

        return not (self.max_size is not None and size > self.max_size)


class ContentFilter(FileFilter):
    """Filter that matches files based on their content."""

    def __init__(
        self,
        pattern: str | Pattern | Callable[[str], bool],
        max_size: int | None = 1024 * 1024,  # Default: 1MB
        encoding: str = "utf-8",
    ) -> None:
        """
        Initialize a content filter.

        Args:
            pattern: String pattern, compiled regex, or callback function to match content
            max_size: Maximum file size to read, or None for no limit
            encoding: File encoding to use when reading
        """
        self.max_size = max_size
        self.encoding = encoding

        # Properly type the matcher function
        self.matcher: Callable[[str], bool]

        if isinstance(pattern, str):
            regex = re.compile(pattern)
            self.matcher = lambda text: bool(regex.search(text))
        elif hasattr(pattern, "search"):
            # Create a wrapper function to handle the overloaded method
            self.matcher = lambda text: bool(pattern.search(text))
        else:
            self.matcher = pattern

    def matches(self, file_path: Path) -> bool:
        if not file_path.is_file():
            return False

        # Check file size if max_size is set
        if self.max_size is not None:
            size = file_path.stat().st_size
            if size > self.max_size:
                return False

        try:
            # Read the file content
            with open(file_path, encoding=self.encoding) as f:
                content = f.read()

            # Match the content
            return bool(self.matcher(content))
        except (OSError, UnicodeDecodeError):
            # If we can't read the file, assume it doesn't match
            return False


class FilterBuilder:
    """Utility for building complex file filters."""

    @staticmethod
    def from_patterns(patterns: FilePatterns) -> FileFilter:
        """Create a filter from FilePatterns."""
        return PatternFilter(patterns)

    @staticmethod
    def from_config(config) -> FileFilter:
        """Create a filter from RepoInsightConfig."""
        # Create the base pattern filter
        pattern_filter = PatternFilter(config.file_patterns)

        # Create filters for excluded directories
        excluded_dirs = config.exclude_directories

        def directory_filter(path: Path) -> bool:
            # Check if any part of the path is in excluded_dirs
            path_parts = path.parts
            return not any(part in excluded_dirs for part in path_parts)

        # Combine pattern filter with directory exclusion
        return AndFilter(pattern_filter, LambdaFilter(directory_filter))

    @staticmethod
    def binary_filter() -> FileFilter:
        """Create a filter that excludes binary files."""
        return NotFilter(ContentFilter(lambda content: b"\0" in content[:1024].encode()))

    @staticmethod
    def size_filter(max_size: int) -> FileFilter:
        """Create a filter that excludes files larger than max_size."""
        return SizeFilter(max_size=max_size)


class LambdaFilter(FileFilter):
    """Filter that uses a custom function to determine matches."""

    def __init__(self, func: Callable[[Path], bool]) -> None:
        """
        Initialize a lambda filter.

        Args:
            func: Function that takes a Path and returns True if it matches
        """
        self.func = func

    def matches(self, file_path: Path) -> bool:
        return self.func(file_path)

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_core_engine_py_16"></a>

## File: src/repoinsight/core/engine.py

**Language**: python

### Description

This code implements a core processing engine for RepoInsight that scans repositories, extracts metadata, generates file descriptions using an LLM, and produces Markdown documentation.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 7.7 KB                     |
| **Last Modified** | 2025-04-16T19:05:52.333138 |
| **Type**          | py                         |

```python
"""
Core processing engine for RepoInsight.

This module provides the main processing engine that orchestrates
the entire workflow of the application.
"""

import asyncio
import logging
import os
from pathlib import Path

from repoinsight.config.models import RepoInsightConfig
from repoinsight.core.models import FileData, RepositorySnapshot
from repoinsight.git.metadata import GitMetadataExtractor
from repoinsight.git.repository import GitRepository
from repoinsight.llm.client import LLMClient
from repoinsight.markdown.generator import MarkdownGenerator
from repoinsight.scanner.engine import FileTypeDetector, RepositoryScanner

logger = logging.getLogger(__name__)


class ProcessingEngine:
    """
    Main processing engine for RepoInsight.

    This class orchestrates the entire workflow, from scanning files
    to generating descriptions and producing the final markdown output.
    """

    def __init__(self, config: RepoInsightConfig) -> None:
        """
        Initialize the processing engine.

        Args:
            config: Configuration for the engine
        """
        self.config = config
        self.max_concurrency = min(os.cpu_count() or 4, config.processing.max_concurrent_tasks)
        self.semaphore = asyncio.Semaphore(self.max_concurrency)

        # Initialize components
        self.llm_client: LLMClient | None = None  # Properly typed to allow None or LLMClient
        self._init_components()

    def _init_components(self) -> None:
        """Initialize the various components based on configuration."""
        # Initialize Git repository
        self.repository = GitRepository(self.config.get_absolute_root_path())
        self.metadata_extractor = GitMetadataExtractor(self.repository)

        # Initialize LLM client if enabled
        if self.config.llm.enabled:
            cache_dir = (
                self.config.get_absolute_cache_path() if self.config.llm.cache_enabled else None
            )
            self.llm_client = LLMClient(
                base_url=self.config.llm.api_base_url,
                api_key=self.config.llm.api_key,
                timeout=self.config.llm.timeout,
                cache_dir=cache_dir,
            )
        else:
            self.llm_client = None

        # Initialize scanner
        self.scanner = RepositoryScanner(
            self.config.get_absolute_root_path(),
            self.config.file_patterns,
            self.config.exclude_directories,
            self.config.scan_directories,
        )

        # Initialize markdown generator
        self.markdown_generator = MarkdownGenerator(
            include_toc=self.config.output.include_toc,
            include_metadata=self.config.output.include_metadata,
            include_file_stats=self.config.output.include_file_stats,
            include_commit_info=self.config.output.include_commit_info,
            syntax_highlighting=self.config.output.syntax_highlighting,
        )

    async def process_repository(self) -> RepositorySnapshot:
        """
        Process the repository and generate a snapshot.

        Returns:
            Repository snapshot with all processed files
        """
        logger.info(f"Processing repository: {self.config.root_path}")

        # Create repository snapshot
        snapshot = RepositorySnapshot(
            name=self.config.name,
            root_path=self.config.root_path,
        )

        # Extract repository metadata
        snapshot.metadata = await self.metadata_extractor.extract_repository_metadata()

        # Scan for files
        files = await self.scanner.scan_async()
        logger.info(f"Found {len(files)} files to process")

        # Process files with controlled concurrency
        tasks = []
        for file_path in files:
            task = self._process_file_with_semaphore(file_path)
            tasks.append(task)

        file_results = await asyncio.gather(*tasks, return_exceptions=True)

        # Filter and handle exceptions
        for i, result in enumerate(file_results):
            if isinstance(result, Exception):
                logger.error(f"Error processing {files[i]}: {result}")
            else:
                snapshot.add_file(result)

        logger.info(f"Successfully processed {len(snapshot.files)} files")
        return snapshot

    async def _process_file_with_semaphore(self, file_path: Path) -> FileData:
        """
        Process a file with semaphore-controlled concurrency.

        Args:
            file_path: Path to the file

        Returns:
            Processed file data
        """
        async with self.semaphore:
            return await self._process_file(file_path)

    async def _process_file(self, file_path: Path) -> FileData:
        """
        Process a single file.

        Args:
            file_path: Path to the file

        Returns:
            Processed file data
        """
        logger.debug(f"Processing file: {file_path}")

        try:
            # Read file content
            with open(file_path, encoding="utf-8", errors="replace") as f:
                content = f.read()

            # Get file metadata
            metadata = await self.metadata_extractor.generate_file_metadata(file_path)

            # Detect language
            language = FileTypeDetector.detect_language(file_path)

            # Generate description if LLM is enabled
            description = None
            if self.llm_client and self.config.llm.enabled:
                # Get commit hash for caching if available
                commit_hash = None
                if self.repository.is_git_repository():
                    commit_hash = self.repository.get_head_commit_hash()

                # Generate description
                description = await self.llm_client.generate_description(
                    file_path=file_path,
                    file_content=content,
                    language=language,
                    model=self.config.llm.model,
                    temperature=self.config.llm.temperature,
                    max_tokens=self.config.llm.max_tokens,
                    system_prompt_template=self.config.llm.system_prompt_template,
                    commit_hash=commit_hash,
                )

            # Create and return file data
            return FileData(
                path=file_path,
                content=content,
                description=description,
                metadata=metadata,
            )
        except Exception as e:
            logger.error(f"Error processing file {file_path}: {e}")
            raise

    async def generate_markdown(self, snapshot: RepositorySnapshot) -> str:
        """
        Generate Markdown documentation from a repository snapshot.

        Args:
            snapshot: Repository snapshot

        Returns:
            Markdown document
        """
        return self.markdown_generator.generate(snapshot.to_dict())

    async def process_and_generate(self) -> tuple[RepositorySnapshot, str]:
        """
        Process the repository and generate Markdown documentation.

        Returns:
            Tuple of repository snapshot and Markdown document
        """
        # Process repository
        snapshot = await self.process_repository()

        # Generate markdown
        markdown = await self.generate_markdown(snapshot)

        # Save output if path is specified
        if self.config.output_path:
            output_path = self.config.get_absolute_output_path()
            if output_path:
                # Ensure directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Write markdown to file
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(markdown)

                logger.info(f"Markdown saved to: {output_path}")

        return snapshot, markdown

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_core___init___py_17"></a>

## File: src/repoinsight/core/**init**.py

**Language**: python

### Description

This Python package serves as the central processing engine for RepoInsight, managing repository analysis workflows.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 357 bytes                  |
| **Last Modified** | 2025-04-16T16:56:41.459664 |
| **Type**          | py                         |

```python
"""
Core processing package for RepoInsight.

This package provides the main processing engine that orchestrates
the entire workflow of the application.
"""

from repoinsight.core.engine import ProcessingEngine
from repoinsight.core.models import FileData, RepositorySnapshot

__all__ = [
    "ProcessingEngine",
    "FileData",
    "RepositorySnapshot",
]

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_core_models_py_18"></a>

## File: src/repoinsight/core/models.py

**Language**: python

### Description

This code defines data models for representing files and repositories within a processing engine.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 4.9 KB                     |
| **Last Modified** | 2025-04-16T19:04:26.824106 |
| **Type**          | py                         |

```python
"""
Data models for the RepoInsight core processing engine.

This module defines the data structures used to represent files, repositories,
and other entities in the processing pipeline.
"""

import datetime
from pathlib import Path


class FileData:
    """
    Data structure representing a file in the repository.
    """

    def __init__(
        self,
        path: str | Path,
        content: str | None = None,
        description: str | None = None,
        metadata: dict | None = None,
    ) -> None:
        """
        Initialize file data.

        Args:
            path: Path to the file
            content: File content
            description: Generated description
            metadata: File metadata
        """
        self.path = str(path)
        self.content = content
        self.description = description
        self.metadata = metadata or {}

    def to_dict(self) -> dict:
        """
        Convert to a dictionary representation.

        Returns:
            Dictionary representation
        """
        return {
            "path": self.path,
            "content": self.content,
            "description": self.description,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "FileData":
        """
        Create a FileData instance from a dictionary.

        Args:
            data: Dictionary representation

        Returns:
            FileData instance
        """
        return cls(
            path=data["path"],
            content=data.get("content"),
            description=data.get("description"),
            metadata=data.get("metadata"),
        )


class RepositorySnapshot:
    """
    Data structure representing a snapshot of a repository.
    """

    def __init__(
        self,
        name: str,
        root_path: str | Path,
        files: list[FileData] | None = None,
        metadata: dict | None = None,
        generation_timestamp: str | None = None,
    ) -> None:
        """
        Initialize repository snapshot.

        Args:
            name: Repository name
            root_path: Repository root path
            files: List of files
            metadata: Repository metadata
            generation_timestamp: When the snapshot was generated
        """
        self.name = name
        self.root_path = str(root_path)
        self.files = files or []
        self.metadata = metadata or {}

        # Use provided timestamp or generate a new one
        if generation_timestamp:
            self.generation_timestamp = generation_timestamp
        else:
            self.generation_timestamp = datetime.datetime.now().isoformat()

    def add_file(self, file_data: FileData) -> None:
        """
        Add a file to the repository snapshot.

        Args:
            file_data: File data to add
        """
        self.files.append(file_data)

    def to_dict(self) -> dict:
        """
        Convert to a dictionary representation.

        Returns:
            Dictionary representation
        """
        return {
            "name": self.name,
            "root_path": self.root_path,
            "files": [file.to_dict() for file in self.files],
            "metadata": self.metadata,
            "generation_timestamp": self.generation_timestamp,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "RepositorySnapshot":
        """
        Create a RepositorySnapshot instance from a dictionary.

        Args:
            data: Dictionary representation

        Returns:
            RepositorySnapshot instance
        """
        files = [FileData.from_dict(file_data) for file_data in data.get("files", [])]

        return cls(
            name=data["name"],
            root_path=data["root_path"],
            files=files,
            metadata=data.get("metadata"),
            generation_timestamp=data.get("generation_timestamp"),
        )

    def save_to_file(self, file_path: str | Path) -> None:
        """
        Save the repository snapshot to a JSON file.

        Args:
            file_path: Path to save the file to
        """
        import json
        from pathlib import Path

        # Convert to dictionary
        snapshot_dict = self.to_dict()

        # Ensure directory exists
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        # Write to file
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snapshot_dict, f, indent=2)

    @classmethod
    def load_from_file(cls, file_path: str | Path) -> "RepositorySnapshot":
        """
        Load a repository snapshot from a JSON file.

        Args:
            file_path: Path to the file

        Returns:
            RepositorySnapshot instance
        """
        import json

        # Read from file
        with open(file_path, encoding="utf-8") as f:
            snapshot_dict = json.load(f)

        # Create instance
        return cls.from_dict(snapshot_dict)

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_markdown_generator_py_19"></a>

## File: src/repoinsight/markdown/generator.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 10.0 KB                    |
| **Last Modified** | 2025-04-16T19:17:32.102993 |
| **Type**          | py                         |

```python
"""
Markdown document generation for RepoInsight.

This module provides functionality for generating complete Markdown documentation
from repository files and metadata.
"""

import re
from pathlib import Path

from repoinsight.markdown.components import MarkdownComponents


class MarkdownGenerator:
    """
    Generator for Markdown documentation from repository files.
    """

    def __init__(
        self,
        include_toc: bool = True,
        include_metadata: bool = True,
        include_file_stats: bool = True,
        include_commit_info: bool = True,
        syntax_highlighting: bool = True,
    ) -> None:
        """
        Initialize a Markdown generator.

        Args:
            include_toc: Whether to include a table of contents
            include_metadata: Whether to include repository metadata
            include_file_stats: Whether to include file statistics
            include_commit_info: Whether to include commit information
            syntax_highlighting: Whether to use syntax highlighting
        """
        self.include_toc = include_toc
        self.include_metadata = include_metadata
        self.include_file_stats = include_file_stats
        self.include_commit_info = include_commit_info
        self.syntax_highlighting = syntax_highlighting

    def generate(self, repository_snapshot: dict) -> str:
        """
        Generate a complete Markdown document for a repository snapshot.

        Args:
            repository_snapshot: Repository snapshot data

        Returns:
            Complete Markdown document
        """
        sections = []

        # Add title
        if "name" in repository_snapshot:
            title = f"{repository_snapshot['name']} Documentation"
        else:
            title = "Repository Documentation"

        sections.append(MarkdownComponents.header(title, 1))

        # Add metadata section
        if self.include_metadata and "metadata" in repository_snapshot:
            sections.append(self._generate_metadata_section(repository_snapshot["metadata"]))

        # Generate file sections and collect TOC entries
        file_sections = []
        toc_entries = []

        if "files" in repository_snapshot and repository_snapshot["files"]:
            # Create an ID counter for generating unique anchors
            id_counter = 0

            for file_data in repository_snapshot["files"]:
                # Generate a unique file ID for anchoring
                file_id = self._generate_file_id(file_data["path"], id_counter)
                id_counter += 1

                # Generate the file section
                file_section = self._generate_file_section(
                    file_data,
                    file_id,
                    repository_snapshot.get("root_path", ""),
                )

                # Add to file sections
                file_sections.append(file_section)

                # Add to TOC entries
                toc_entry = self._generate_toc_entry(
                    file_data["path"],
                    file_id,
                    repository_snapshot.get("root_path", ""),
                )
                toc_entries.append(toc_entry)

        # Add TOC if enabled and we have files
        if self.include_toc and toc_entries:
            sections.append(self._generate_toc(toc_entries))

        # Add all file sections
        sections.extend(file_sections)

        # Add generation info
        if "generation_timestamp" in repository_snapshot:
            sections.append(self._generate_generation_info(repository_snapshot))

        # Join all sections
        return "\n".join(sections)

    def _generate_metadata_section(self, metadata: dict) -> str:
        """
        Generate the repository metadata section.

        Args:
            metadata: Repository metadata

        Returns:
            Formatted metadata section
        """
        section = MarkdownComponents.header("Repository Information", 2)

        # Format the metadata as a series of sections
        for section_name, section_data in metadata.items():
            if isinstance(section_data, dict):
                section += MarkdownComponents.header(section_name, 3)

                # Convert the section data to a list of key-value pairs
                formatted_data = {}
                for key, value in section_data.items():
                    # Format value based on its type
                    if isinstance(value, list):
                        formatted_value = ", ".join(map(str, value))
                    else:
                        formatted_value = str(value)

                    formatted_data[key] = formatted_value

                section += MarkdownComponents.metadata_table(formatted_data)

        return section

    def _generate_file_section(self, file_data: dict, file_id: str, root_path: str) -> str:
        """
        Generate a section for a single file.

        Args:
            file_data: File data
            file_id: Unique file ID for anchoring
            root_path: Repository root path

        Returns:
            Formatted file section
        """
        # Extract file data
        file_path = file_data["path"]
        file_content = file_data.get("content", "")
        file_description = file_data.get("description", "")
        file_metadata = file_data.get("metadata", {})

        # Start with the file header
        section = f'<a id="{file_id}"></a>\n\n'  # Add anchor
        section += MarkdownComponents.file_header(file_path, root_path)

        # Add description if available
        if file_description:
            section += MarkdownComponents.file_description(file_description)

        # Add metadata if enabled and available
        if self.include_file_stats and file_metadata:
            # Format metadata for display
            formatted_metadata = {}

            # Basic file stats
            if "size_bytes" in file_metadata:
                formatted_metadata["Size"] = self._format_file_size(file_metadata["size_bytes"])

            if "last_modified" in file_metadata:
                formatted_metadata["Last Modified"] = file_metadata["last_modified"]

            if "extension" in file_metadata:
                formatted_metadata["Type"] = file_metadata["extension"]

            # Git history if available and enabled
            if self.include_commit_info and "git_history" in file_metadata:
                history = file_metadata["git_history"]

                if "last_commit" in history:
                    commit = history["last_commit"]
                    formatted_metadata[
                        "Last Commit"
                    ] = f"{commit['short_hash']} - {commit['message']}"
                    formatted_metadata["Author"] = commit["author"]
                    formatted_metadata["Date"] = commit["date"]

                if "commit_count" in history:
                    formatted_metadata["Commit Count"] = str(history["commit_count"])

            # Add metadata table
            if formatted_metadata:
                section += MarkdownComponents.file_metadata(formatted_metadata)

        # Add file content
        if file_content:
            section += MarkdownComponents.file_content(
                file_path,
                file_content,
                self.syntax_highlighting,
            )

        return section

    def _generate_toc(self, toc_entries: list[dict]) -> str:
        """
        Generate a table of contents.

        Args:
            toc_entries: List of TOC entries

        Returns:
            Formatted table of contents
        """
        toc = MarkdownComponents.toc_title()

        # Add each TOC entry
        for entry in toc_entries:
            toc += MarkdownComponents.toc_entry(
                entry["title"],
                entry["link"],
                entry.get("level", 0),
            )

        return toc + "\n"

    def _generate_toc_entry(self, file_path: str, file_id: str, root_path: str) -> dict:
        """
        Generate a table of contents entry for a file.

        Args:
            file_path: Path to the file
            file_id: Unique file ID for linking
            root_path: Repository root path

        Returns:
            TOC entry as a dictionary
        """
        path = Path(file_path)

        # Make path relative if possible
        if root_path:
            try:
                display_path = path.relative_to(root_path)
            except ValueError:
                display_path = path
        else:
            display_path = path

        # Create the TOC entry
        return {
            "title": str(display_path),
            "link": f"#{file_id}",
            "level": len(display_path.parts) - 1,  # Indent based on path depth
        }

    def _generate_file_id(self, file_path: str, counter: int) -> str:
        """
        Generate a unique ID for a file.

        Args:
            file_path: Path to the file
            counter: Unique counter

        Returns:
            Unique file ID
        """
        # Convert path to a safe string for use as an HTML ID
        safe_path = re.sub(r"[^a-zA-Z0-9-]", "_", str(file_path))

        # Append counter to ensure uniqueness
        return f"file_{safe_path}_{counter}"

    def _generate_generation_info(self, repository_snapshot: dict) -> str:
        """
        Generate information about when the documentation was generated.

        Args:
            repository_snapshot: Repository snapshot data

        Returns:
            Formatted generation info
        """
        timestamp = repository_snapshot.get("generation_timestamp", "")

        if not timestamp:
            return ""

        return f"\n\n---\n\nGenerated at: {timestamp}\n"

    @staticmethod
    def _format_file_size(size_bytes: int) -> str:
        """Format file size in a human-readable way."""
        if size_bytes < 1024:
            return f"{size_bytes} bytes"
        if size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        if size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_markdown_components_py_20"></a>

## File: src/repoinsight/markdown/components.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 8.8 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.389077 |
| **Type**          | py                         |

````python
"""
Markdown component generation for RepoInsight.

This module provides building blocks for generating various components
of the Markdown documentation.
"""

import contextlib
from pathlib import Path

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
    def file_header(file_path: str | Path, relative_to: str | Path | None = None) -> str:
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
            with contextlib.suppress(ValueError):
                path = path.relative_to(relative_to)
                # If ValueError is raised, path remains unchanged (absolute)

        # Get file language
        language = FileTypeDetector.detect_language(path)

        # Create header
        header = f"## File: {path}\n\n"
        header += f"**Language**: {language}\n\n"

        return header

    @staticmethod
    def file_content(file_path: str | Path, content: str, syntax_highlighting: bool = True) -> str:
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

````

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_markdown___init___py_21"></a>

## File: src/repoinsight/markdown/**init**.py

**Language**: python

### Description

This Python package generates Markdown documentation from repository data for RepoInsight.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 355 bytes                  |
| **Last Modified** | 2025-04-16T16:56:28.814947 |
| **Type**          | py                         |

```python
"""
Markdown generation package for RepoInsight.

This package provides functionality for generating Markdown documentation
from repository files and metadata.
"""

from repoinsight.markdown.components import MarkdownComponents
from repoinsight.markdown.generator import MarkdownGenerator

__all__ = [
    "MarkdownComponents",
    "MarkdownGenerator",
]

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_config_yaml_py_22"></a>

## File: src/repoinsight/config/yaml.py

**Language**: python

### Description

This code manages RepoInsight configurations by loading, saving, and managing profiles using YAML files and Pydantic models.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 6.6 KB                     |
| **Last Modified** | 2025-04-16T19:04:51.318579 |
| **Type**          | py                         |

```python
"""
YAML configuration handling for RepoInsight.

This module provides functionality to load and save configuration files in YAML format,
with proper validation using the Pydantic models.
"""

import logging
import os
from pathlib import Path

import yaml  # type: ignore
from pydantic import ValidationError

from repoinsight.config.models import RepoInsightConfig

logger = logging.getLogger(__name__)


def load_config(config_path: str | Path) -> RepoInsightConfig:
    """
    Load and validate a configuration file.

    Args:
        config_path: Path to the YAML configuration file

    Returns:
        Validated RepoInsightConfig instance

    Raises:
        FileNotFoundError: If the configuration file does not exist
        ValidationError: If the configuration is invalid
        yaml.YAMLError: If the YAML file is malformed
    """
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, encoding="utf-8") as f:
        config_data = yaml.safe_load(f)

    try:
        return RepoInsightConfig(**config_data)
    except ValidationError as e:
        # Re-raise with more context
        error_msg = f"Invalid configuration in {config_path}: {e.errors()}"
        logger.error(error_msg)
        raise ValidationError(
            e.errors()
        ) from e  # Re-use only the errors from the original ValidationError


def save_config(config: RepoInsightConfig, config_path: str | Path) -> None:
    """
    Save a configuration to a YAML file.

    Args:
        config: RepoInsightConfig instance to save
        config_path: Path to save the configuration to

    Raises:
        IOError: If the file cannot be written
    """
    config_path = Path(config_path)

    # Ensure directory exists
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert to dict and save as YAML
    config_dict = config.model_dump()

    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config_dict, f, default_flow_style=False, sort_keys=False)


def find_config_file(
    directory: str | Path | None = None,
    config_names: list[str] | None = None,
) -> Path | None:
    """
    Find a configuration file in the specified directory or its parents.

    Args:
        directory: Starting directory (defaults to current directory)
        config_names: List of possible config file names (defaults to standard names)

    Returns:
        Path to the first found configuration file, or None if not found
    """
    directory = Path.cwd() if directory is None else Path(directory)

    if config_names is None:
        config_names = [
            ".repoinsight.yml",
            ".repoinsight.yaml",
            "repoinsight.yml",
            "repoinsight.yaml",
        ]

    # Look in the current directory and its parents
    current_dir = directory.absolute()
    while True:
        for name in config_names:
            config_path = current_dir / name
            if config_path.exists():
                return config_path

        # Move to parent directory
        parent_dir = current_dir.parent
        if parent_dir == current_dir:  # Reached root
            break
        current_dir = parent_dir

    return None


def get_user_config_dir() -> Path:
    """
    Get the user configuration directory for RepoInsight.

    Returns:
        Path to the user configuration directory
    """
    # Use platform-specific config directories
    if os.name == "nt":  # Windows
        config_dir = Path(os.environ.get("APPDATA", "")) / "RepoInsight"
    else:  # Unix-like
        xdg_config_home = os.environ.get("XDG_CONFIG_HOME")
        if xdg_config_home:
            config_dir = Path(xdg_config_home) / "repoinsight"
        else:
            config_dir = Path.home() / ".config" / "repoinsight"

    # Ensure directory exists
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


class ConfigManager:
    """
    Manager for RepoInsight configurations with profile support.
    """

    def __init__(self, config_dir: str | Path | None = None) -> None:
        self.config_dir = Path(config_dir) if config_dir else get_user_config_dir()
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_dir = self.config_dir / "profiles"
        self.profiles_dir.mkdir(exist_ok=True)

    def get_available_profiles(self) -> list[str]:
        """Get a list of available configuration profiles."""
        profiles = []
        for file in self.profiles_dir.glob("*.yml"):
            profiles.append(file.stem)
        for file in self.profiles_dir.glob("*.yaml"):
            profiles.append(file.stem)
        return sorted(profiles)

    def load_profile(self, profile_name: str) -> RepoInsightConfig:
        """
        Load a configuration profile.

        Args:
            profile_name: Name of the profile to load

        Returns:
            RepoInsightConfig instance

        Raises:
            FileNotFoundError: If the profile does not exist
        """
        # Try both .yml and .yaml extensions
        yaml_path = self.profiles_dir / f"{profile_name}.yml"
        if not yaml_path.exists():
            yaml_path = self.profiles_dir / f"{profile_name}.yaml"

        if not yaml_path.exists():
            raise FileNotFoundError(f"Profile not found: {profile_name}")

        return load_config(yaml_path)

    def save_profile(self, config: RepoInsightConfig, profile_name: str | None = None) -> None:
        """
        Save a configuration profile.

        Args:
            config: RepoInsightConfig instance to save
            profile_name: Name of the profile (defaults to config.name)
        """
        name = profile_name or config.name
        yaml_path = self.profiles_dir / f"{name}.yml"
        save_config(config, yaml_path)

    def delete_profile(self, profile_name: str) -> bool:
        """
        Delete a configuration profile.

        Args:
            profile_name: Name of the profile to delete

        Returns:
            True if the profile was deleted, False if it did not exist
        """
        # Try both .yml and .yaml extensions
        for ext in [".yml", ".yaml"]:
            path = self.profiles_dir / f"{profile_name}{ext}"
            if path.exists():
                path.unlink()
                return True
        return False

    def load_default_config(self) -> RepoInsightConfig:
        """
        Load the default configuration.

        Returns:
            RepoInsightConfig instance with default values and current directory as root
        """
        return RepoInsightConfig(
            name="Default",
            root_path=str(Path.cwd()),
        )

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_config___init___py_23"></a>

## File: src/repoinsight/config/**init**.py

**Language**: python

### Description

This Python package facilitates managing RepoInsight’s configuration settings, including file patterns and LLM parameters.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 643 bytes                  |
| **Last Modified** | 2025-04-16T16:49:01.305927 |
| **Type**          | py                         |

```python
"""
Configuration package for RepoInsight.

This package provides functionality for managing application configuration settings.
"""

from repoinsight.config.models import (
    FilePatterns,
    LLMConfig,
    OutputConfig,
    ProcessingConfig,
    RepoInsightConfig,
)
from repoinsight.config.yaml import (
    ConfigManager,
    find_config_file,
    get_user_config_dir,
    load_config,
    save_config,
)

__all__ = [
    "FilePatterns",
    "LLMConfig",
    "OutputConfig",
    "ProcessingConfig",
    "RepoInsightConfig",
    "ConfigManager",
    "find_config_file",
    "get_user_config_dir",
    "load_config",
    "save_config",
]

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_config_models_py_24"></a>

## File: src/repoinsight/config/models.py

**Language**: python

### Description

This code defines Pydantic models for configuring the RepoInsight application, including file scanning and LLM integration settings.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 4.8 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.388706 |
| **Type**          | py                         |

```python
"""
Configuration models for RepoInsight.

This module defines the Pydantic models used for validating and parsing configuration
settings for the RepoInsight application.
"""

from pathlib import Path

from pydantic import BaseModel, Field


class FilePatterns(BaseModel):
    """File pattern configuration for including/excluding files during scanning."""

    include: list[str] = Field(
        default_factory=lambda: ["*.py", "*.js", "*.html", "*.css", "*.md"],
        description="Glob patterns to include files",
    )
    exclude: list[str] = Field(
        default_factory=lambda: ["*__pycache__*", "*.git*", "*.pyc", "node_modules/*"],
        description="Glob patterns to exclude files",
    )


class LLMConfig(BaseModel):
    """Configuration for LLM integration."""

    enabled: bool = Field(default=True, description="Enable or disable LLM integration")
    provider: str = Field(default="cortex", description="LLM provider (cortex, openai, etc.)")
    api_base_url: str = Field(
        default="http://localhost:8000/v1", description="Base URL for the LLM API"
    )
    api_key: str | None = Field(default=None, description="API key for the LLM service")
    model: str = Field(default="llama3", description="Model to use for generation")
    temperature: float = Field(default=0.3, description="Temperature for text generation (0.0-1.0)")
    max_tokens: int = Field(default=500, description="Maximum number of tokens to generate")
    timeout: int = Field(default=30, description="API request timeout in seconds")
    cache_enabled: bool = Field(default=True, description="Enable caching of LLM responses")
    system_prompt_template: str = Field(
        default=(
            "Analyze the following {language} code and provide a concise description as markdown."
            "Focus on the main purpose, key functionality and important patterns or techniques used."
            "Keep the description under 5 sentences."
        ),
        description="System prompt template for the LLM",
    )


class ProcessingConfig(BaseModel):
    """Configuration for processing behavior."""

    max_concurrent_tasks: int = Field(
        default=4, description="Maximum number of concurrent processing tasks"
    )
    chunk_size: int = Field(
        default=8192, description="Maximum chunk size in bytes for processing files"
    )


class OutputConfig(BaseModel):
    """Configuration for output formatting."""

    include_toc: bool = Field(default=True, description="Include table of contents in output")
    include_metadata: bool = Field(default=True, description="Include metadata in output")
    include_file_stats: bool = Field(default=True, description="Include file statistics in output")
    include_commit_info: bool = Field(
        default=True, description="Include commit information in output"
    )
    syntax_highlighting: bool = Field(
        default=True, description="Enable syntax highlighting in output"
    )


class RepoInsightConfig(BaseModel):
    """Main configuration model for RepoInsight."""

    name: str = Field(..., description="Name of the configuration profile")
    root_path: str = Field(..., description="Root path of the repository or directory")
    output_path: str | None = Field(
        default=None, description="Output path for the generated documentation"
    )
    scan_directories: list[str] = Field(
        default_factory=lambda: ["."],
        description="Directories to scan relative to root_path",
    )
    exclude_directories: list[str] = Field(
        default_factory=lambda: ["venv", "node_modules", ".git"],
        description="Directories to exclude from scanning",
    )
    file_patterns: FilePatterns = Field(
        default_factory=FilePatterns, description="File patterns for scanning"
    )
    llm: LLMConfig = Field(default_factory=LLMConfig, description="LLM integration configuration")
    processing: ProcessingConfig = Field(
        default_factory=ProcessingConfig, description="Processing configuration"
    )
    output: OutputConfig = Field(default_factory=OutputConfig, description="Output configuration")
    cache_path: str = Field(default=".repoinsight_cache", description="Path for caching data")

    def get_absolute_root_path(self) -> Path:
        """Get the absolute path to the repository root."""
        return Path(self.root_path).absolute()

    def get_absolute_output_path(self) -> Path | None:
        """Get the absolute path to the output file, if specified."""
        if not self.output_path:
            return None
        return Path(self.output_path).absolute()

    def get_absolute_cache_path(self) -> Path:
        """Get the absolute path to the cache directory."""
        # If cache_path is relative, make it relative to the root_path
        cache_path = Path(self.cache_path)
        if not cache_path.is_absolute():
            return Path(self.root_path) / cache_path
        return cache_path

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_config_panel_py_25"></a>

## File: src/repoinsight/gui/config_panel.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 22.6 KB                    |
| **Last Modified** | 2025-04-16T20:50:50.388920 |
| **Type**          | py                         |

```python
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

    def __init__(self, parent: QWidget | None = None) -> None:
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

        if not directory:
            return

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
        existing_items = [
            self.scan_dirs_list.item(i).text() for i in range(self.scan_dirs_list.count())
        ]
        if directory not in existing_items:
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

        if not directory:
            return

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
        existing_items = [
            self.exclude_dirs_list.item(i).text() for i in range(self.exclude_dirs_list.count())
        ]
        if directory not in existing_items:
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

        # Use a single if statement with logical AND
        existing_patterns = [
            self.include_patterns_list.item(i).text()
            for i in range(self.include_patterns_list.count())
        ]
        if ok and pattern and pattern not in existing_patterns:
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

        # Use a single if statement with logical AND
        existing_patterns = [
            self.exclude_patterns_list.item(i).text()
            for i in range(self.exclude_patterns_list.count())
        ]
        if ok and pattern and pattern not in existing_patterns:
            self.exclude_patterns_list.addItem(pattern)

    def _remove_exclude_pattern(self) -> None:
        """Remove an exclude pattern."""
        selected_items = self.exclude_patterns_list.selectedItems()
        for item in selected_items:
            self.exclude_patterns_list.takeItem(self.exclude_patterns_list.row(item))

    def set_config(self, config: RepoInsightConfig) -> None:
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

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_worker_py_26"></a>

## File: src/repoinsight/gui/worker.py

**Language**: python

### Description

This code defines asynchronous worker classes for running long-running tasks in the RepoInsight GUI, handling operations like documentation generation.<end_of_turn>

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 4.6 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.389077 |
| **Type**          | py                         |

```python
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

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_preview_panel_py_27"></a>

## File: src/repoinsight/gui/preview_panel.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 6.7 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.389005 |
| **Type**          | py                         |

```python
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

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_profile_panel_py_28"></a>

## File: src/repoinsight/gui/profile_panel.py

**Language**: python

### Description

Error generating description:

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 12.4 KB                    |
| **Last Modified** | 2025-04-16T20:50:50.389037 |
| **Type**          | py                         |

```python
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

    def __init__(self, config_manager: "ConfigManager", parent: QWidget | None = None) -> None:
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

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui___init___py_29"></a>

## File: src/repoinsight/gui/**init**.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 602 bytes                  |
| **Last Modified** | 2025-04-16T18:02:19.235246 |
| **Type**          | py                         |

```python
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

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_app_py_30"></a>

## File: src/repoinsight/gui/app.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 5.7 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.388706 |
| **Type**          | py                         |

```python
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

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_gui_main_window_py_31"></a>

## File: src/repoinsight/gui/main_window.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 11.0 KB                    |
| **Last Modified** | 2025-04-16T20:50:50.388965 |
| **Type**          | py                         |

```python
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
        # Clean up worker thread if running
        if hasattr(self, "_worker") and self._worker and self._worker.is_running():
            self._worker.stop()

        # In a real implementation, we would check for unsaved changes
        event.accept()

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm_client_py_32"></a>

## File: src/repoinsight/llm/client.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 10.8 KB                    |
| **Last Modified** | 2025-04-16T20:50:50.389077 |
| **Type**          | py                         |

```python
"""
LLM client for RepoInsight.

This module provides functionality for interacting with language models through
OpenAI-compatible APIs, such as Cortex.
"""

import asyncio
import hashlib
import json
import logging
import time
from pathlib import Path
from typing import Any

import aiohttp

logger = logging.getLogger(__name__)


class LLMClient:
    """
    Client for interacting with LLM APIs using the OpenAI-compatible format.

    Supports local model servers like Cortex and cloud services like OpenAI.
    """

    def __init__(
        self,
        base_url: str = "http://localhost:8000/v1",
        api_key: str | None = None,
        timeout: int = 30,
        max_retries: int = 3,
        retry_delay: int = 2,
        cache_dir: str | Path | None = None,
    ) -> None:
        """
        Initialize an LLM client.

        Args:
            base_url: Base URL for the API
            api_key: API key (if required)
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries on failure
            retry_delay: Delay between retries in seconds
            cache_dir: Directory for caching responses
        """
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.cache_dir = Path(cache_dir) if cache_dir else None

        # Create cache directory if specified
        if self.cache_dir:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_default_headers(self) -> dict[str, str]:
        """Get default headers for API requests."""
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def _get_cache_path(self, cache_key: str) -> Path | None:
        """Get the cache file path for a given key."""
        if not self.cache_dir:
            return None

        # Create a hash of the key for the filename
        key_hash = hashlib.md5(cache_key.encode()).hexdigest()
        return self.cache_dir / f"{key_hash}.json"

    async def _get_from_cache(self, cache_key: str) -> dict[str, Any] | None:
        """Try to get a response from the cache."""
        if not self.cache_dir:
            return None

        cache_path = self._get_cache_path(cache_key)
        if not cache_path or not cache_path.exists():
            return None

        try:
            with open(cache_path, encoding="utf-8") as f:
                cache_data = json.load(f)

            # Check if the cache has expired (if expiration is set)
            if "expiration" in cache_data and cache_data["expiration"] < time.time():
                # Cache expired
                return None

            return cache_data.get("response")
        except (OSError, json.JSONDecodeError) as e:
            logger.warning(f"Error reading cache: {e}")
            return None

    async def _save_to_cache(
        self, cache_key: str, response: dict[str, Any], ttl: int | None = None
    ) -> None:
        """Save a response to the cache."""
        if not self.cache_dir:
            return

        cache_path = self._get_cache_path(cache_key)
        if not cache_path:
            return

        try:
            cache_data = {
                "response": response,
                "timestamp": time.time(),
            }

            # Add expiration if TTL is provided
            if ttl is not None:
                cache_data["expiration"] = time.time() + ttl

            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f)
        except OSError as e:
            logger.warning(f"Error writing to cache: {e}")

    def _compute_cache_key(
        self, model: str, messages: list[dict[str, str]], additional_key: str | None = None
    ) -> str:
        """Compute a cache key for the request."""
        # Create a dictionary of the request parameters
        key_data = {
            "model": model,
            "messages": messages,
        }

        # Add additional key information if provided
        if additional_key:
            key_data["additional_key"] = additional_key

        # Convert to a consistent string representation
        key_str = json.dumps(key_data, sort_keys=True)

        # Return a hash of the key string
        return hashlib.sha256(key_str.encode()).hexdigest()

    async def chat_completion(
        self,
        model: str,
        messages: list[dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int | None = None,
        top_p: float | None = None,
        frequency_penalty: float | None = None,
        presence_penalty: float | None = None,
        stop: str | list[str] | None = None,
        cache_key: str | None = None,
        use_cache: bool = True,
    ) -> dict[str, Any]:
        """
        Send a chat completion request to the API.

        Args:
            model: Model to use for generation
            messages: List of message objects
            temperature: Sampling temperature (0.0-2.0)
            max_tokens: Maximum number of tokens to generate
            top_p: Nucleus sampling parameter
            frequency_penalty: Frequency penalty parameter
            presence_penalty: Presence penalty parameter
            stop: Stop sequence(s) to end generation
            cache_key: Additional information to include in the cache key
            use_cache: Whether to use cache for this request

        Returns:
            API response as a dictionary
        """
        # Prepare the request payload
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        # Add optional parameters if provided
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if top_p is not None:
            payload["top_p"] = top_p
        if frequency_penalty is not None:
            payload["frequency_penalty"] = frequency_penalty
        if presence_penalty is not None:
            payload["presence_penalty"] = presence_penalty
        if stop is not None:
            payload["stop"] = stop

        # Try to get from cache if enabled
        if use_cache and self.cache_dir:
            computed_cache_key = self._compute_cache_key(model, messages, cache_key)
            cached_response = await self._get_from_cache(computed_cache_key)
            if cached_response:
                logger.debug(f"Cache hit for {computed_cache_key}")
                return cached_response

        # Make the API request with retries
        for attempt in range(self.max_retries):
            try:
                async with aiohttp.ClientSession() as session, session.post(
                    f"{self.base_url}/chat/completions",
                    headers=self._get_default_headers(),
                    json=payload,
                    timeout=self.timeout,
                ) as response:
                    if response.status == 200:
                        result = await response.json()

                        # Save to cache if enabled
                        if use_cache and self.cache_dir:
                            await self._save_to_cache(computed_cache_key, result)

                        return result
                    error_text = await response.text()
                    logger.error(
                        f"API error (attempt {attempt+1}/{self.max_retries}): "
                        f"Status {response.status} - {error_text}"
                    )

                    # If we've exhausted retries, raise an exception
                    if attempt == self.max_retries - 1:
                        response.raise_for_status()
            except (TimeoutError, aiohttp.ClientError) as e:
                logger.error(f"Request error (attempt {attempt+1}/{self.max_retries}): {e}")

                # If we've exhausted retries, re-raise the exception
                if attempt == self.max_retries - 1:
                    raise

            # Wait before retrying
            await asyncio.sleep(self.retry_delay * (2**attempt))  # Exponential backoff

        # This should not be reached if max_retries > 0
        raise RuntimeError("Failed to get a response from the API")

    async def generate_description(
        self,
        file_path: str | Path,
        file_content: str,
        language: str,
        model: str = "llama3",
        temperature: float = 0.3,
        max_tokens: int = 500,
        system_prompt_template: str | None = None,
        commit_hash: str | None = None,
    ) -> str:
        """
        Generate a description for a source code file.

        Args:
            file_path: Path to the file
            file_content: Content of the file
            language: Programming language of the file
            model: Model to use for generation
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum number of tokens to generate
            system_prompt_template: Template for system prompt (with {language} placeholder)
            commit_hash: Git commit hash for cache key

        Returns:
            Generated description as a string
        """
        # Use default system prompt template if not provided
        if system_prompt_template is None:
            system_prompt_template = (
                "Analyze the following {language} code and provide a concise description "
                "in markdown format. Focus on the main purpose, key functionality, and "
                "important patterns or techniques used. Keep the description under 5 sentences."
            )

        # Format the system prompt
        system_prompt = system_prompt_template.format(language=language)

        # Prepare messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": file_content},
        ]

        # Create cache key with commit hash if available
        cache_key = None
        if commit_hash:
            path_str = str(file_path)
            cache_key = f"{path_str}:{commit_hash}"

        try:
            # Make the API request
            response = await self.chat_completion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                cache_key=cache_key,
            )

            # Extract and return the generated description
            if "choices" in response and len(response["choices"]) > 0:
                return response["choices"][0]["message"]["content"].strip()

            logger.warning(f"Unexpected response format: {response}")
            return "Error: Unexpected response format from LLM API."
        except Exception as e:
            logger.error(f"Error generating description: {e}")
            return f"Error generating description: {str(e)}"

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm___init___py_33"></a>

## File: src/repoinsight/llm/**init**.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 434 bytes                  |
| **Last Modified** | 2025-04-16T16:54:57.081591 |
| **Type**          | py                         |

```python
"""
LLM integration package for RepoInsight.

This package provides functionality for interacting with language models to
generate descriptions of source code files.
"""

from repoinsight.llm.cache import CacheManager
from repoinsight.llm.client import LLMClient
from repoinsight.llm.prompts import PromptTemplates, get_system_prompt

__all__ = [
    "LLMClient",
    "CacheManager",
    "PromptTemplates",
    "get_system_prompt",
]

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm_prompts_py_34"></a>

## File: src/repoinsight/llm/prompts.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 9.0 KB                     |
| **Last Modified** | 2025-04-16T19:16:59.185132 |
| **Type**          | py                         |

```python
"""
System prompt templates for LLM interactions.

This module provides specialized system prompts for various programming languages
and file types to improve the quality of generated descriptions.
"""


class PromptTemplates:
    """
    Collection of system prompt templates for different programming languages and file types.
    """

    # Default prompt template for any language
    DEFAULT_TEMPLATE = (
        "Analyze the following {language} code and provide a concise description "
        "in markdown format. Focus on the main purpose, key functionality, and "
        "important patterns or techniques used. Keep the description under 5 sentences. "
        "Use technical but clear language appropriate for a software documentation context."
    )

    # Specialized templates for specific languages
    LANGUAGE_TEMPLATES = {
        # Python-specific prompt
        "python": (
            "Analyze the following Python code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The module's main purpose and functionality\n"
            "2. Key classes, functions, and their relationships\n"
            "3. Important design patterns or Python idioms used\n"
            "4. Dependencies and their roles\n"
            "5. Any notable algorithms or techniques\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for Python developers. If appropriate, mention Python-specific "
            "features like decorators, context managers, generators, or async functionality."
        ),
        # JavaScript/TypeScript prompt
        "javascript": (
            "Analyze the following JavaScript code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The module's main purpose and functionality\n"
            "2. Key functions, classes, or components\n"
            "3. Important design patterns or JavaScript idioms used\n"
            "4. Dependencies and their roles\n"
            "5. Any notable frameworks or libraries used\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for JavaScript developers. If appropriate, mention JavaScript-specific "
            "features like closures, promises, async/await, or functional patterns."
        ),
        "typescript": (
            "Analyze the following TypeScript code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The module's main purpose and functionality\n"
            "2. Key interfaces, types, classes, or components\n"
            "3. Important design patterns or TypeScript idioms used\n"
            "4. Type system features being leveraged\n"
            "5. Any notable frameworks or libraries used\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for TypeScript developers. If appropriate, mention TypeScript-specific "
            "features like generics, type guards, utility types, or advanced type constructs."
        ),
        # HTML/CSS prompt
        "html": (
            "Analyze the following HTML code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The document's main purpose and structure\n"
            "2. Key sections, components, or elements\n"
            "3. Important accessibility features\n"
            "4. Integration with other technologies (CSS, JavaScript)\n"
            "5. Any notable frameworks or libraries used\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for web developers."
        ),
        "css": (
            "Analyze the following CSS code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The stylesheet's main purpose and scope\n"
            "2. Key styling patterns or component styles\n"
            "3. Important CSS techniques or methodologies used (e.g., Flexbox, Grid, BEM)\n"
            "4. Responsive design approaches\n"
            "5. Any notable preprocessor features (if using SCSS/LESS)\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for web developers."
        ),
        # Configuration files prompt
        "json": (
            "Analyze the following JSON configuration file and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The configuration's main purpose\n"
            "2. Key sections or settings\n"
            "3. Important options and their significance\n"
            "4. How this configuration relates to the application\n"
            "5. Any notable patterns or structures\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "that explains the purpose and key aspects of this configuration."
        ),
        "yaml": (
            "Analyze the following YAML configuration file and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The configuration's main purpose\n"
            "2. Key sections or settings\n"
            "3. Important options and their significance\n"
            "4. How this configuration relates to the application\n"
            "5. Any notable patterns or structures\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "that explains the purpose and key aspects of this configuration."
        ),
        "toml": (
            "Analyze the following TOML configuration file and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The configuration's main purpose\n"
            "2. Key sections or settings\n"
            "3. Important options and their significance\n"
            "4. How this configuration relates to the application\n"
            "5. Any notable patterns or structures\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "that explains the purpose and key aspects of this configuration."
        ),
        # Documentation files prompt
        "markdown": (
            "Analyze the following Markdown document and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The document's main purpose and topic\n"
            "2. Key sections or headings\n"
            "3. Important information or instructions contained\n"
            "4. The target audience\n"
            "5. Any notable formatting or structure\n\n"
            "Keep the description under 5 sentences. Provide a clear summary that captures "
            "the essence and purpose of this documentation."
        ),
        # Shell scripts prompt
        "bash": (
            "Analyze the following shell script and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The script's main purpose and functionality\n"
            "2. Key commands or operations performed\n"
            "3. Important parameters or environment variables used\n"
            "4. Error handling or validation mechanisms\n"
            "5. Any notable shell-specific techniques\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for system administrators or DevOps engineers."
        ),
    }

    @classmethod
    def get_template(cls, language: str) -> str:
        """
        Get a prompt template for a specific language.

        Args:
            language: The programming language or file type

        Returns:
            A prompt template string with a {language} placeholder
        """
        # Normalize the language name
        norm_language = language.lower()

        # Check for direct language match
        if norm_language in cls.LANGUAGE_TEMPLATES:
            return cls.LANGUAGE_TEMPLATES[norm_language]

        # Check for language aliases
        if norm_language in ["js", "jsx"]:
            return cls.LANGUAGE_TEMPLATES["javascript"]
        if norm_language in ["ts", "tsx"]:
            return cls.LANGUAGE_TEMPLATES["typescript"]
        if norm_language in ["py"]:
            return cls.LANGUAGE_TEMPLATES["python"]
        if norm_language in ["scss", "less"]:
            return cls.LANGUAGE_TEMPLATES["css"]
        if norm_language in ["yml"]:
            return cls.LANGUAGE_TEMPLATES["yaml"]
        if norm_language in ["sh", "shell", "zsh"]:
            return cls.LANGUAGE_TEMPLATES["bash"]
        if norm_language in ["md"]:
            return cls.LANGUAGE_TEMPLATES["markdown"]

        # Fallback to default template
        return cls.DEFAULT_TEMPLATE


def get_system_prompt(language: str) -> str:
    """
    Get a formatted system prompt for a specific language.

    Args:
        language: The programming language or file type

    Returns:
        A formatted system prompt
    """
    template = PromptTemplates.get_template(language)
    return template.format(language=language)

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_llm_cache_py_35"></a>

## File: src/repoinsight/llm/cache.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 6.7 KB                     |
| **Last Modified** | 2025-04-16T19:11:23.294207 |
| **Type**          | py                         |

```python
"""
Caching system for LLM responses.

This module provides a filesystem-based caching system for storing and retrieving
LLM responses, optimized for codebase analysis.
"""

import json
import logging
import time
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class CacheManager:
    """
    File-based cache manager for LLM responses.

    Stores responses in JSON files organized by key, with optional
    expiration times for cache invalidation.
    """

    def __init__(self, cache_dir: str | Path) -> None:
        """
        Initialize a cache manager.

        Args:
            cache_dir: Directory to store cache files
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_path(self, key: str) -> Path:
        """
        Get the path to a cache file for a given key.

        Args:
            key: Cache key

        Returns:
            Path to the cache file
        """
        # Create a safe filename from the key
        safe_key = "".join(c if c.isalnum() else "_" for c in key)
        if len(safe_key) > 100:  # Limit filename length
            import hashlib

            # Use part of the original key + hash for uniqueness
            hash_part = hashlib.md5(key.encode()).hexdigest()
            safe_key = f"{safe_key[:50]}_{hash_part}"

        return self.cache_dir / f"{safe_key}.json"

    async def get(self, key: str) -> Any | None:
        """
        Get a value from the cache.

        Args:
            key: Cache key

        Returns:
            Cached value, or None if not found or expired
        """
        cache_path = self._get_cache_path(key)

        if not cache_path.exists():
            return None

        try:
            with open(cache_path, encoding="utf-8") as f:
                cache_data = json.load(f)

            # Check if the cache has expired
            if "expiration" in cache_data and cache_data["expiration"] < time.time():
                logger.debug(f"Cache expired for key: {key}")
                return None

            logger.debug(f"Cache hit for key: {key}")
            return cache_data.get("value")
        except Exception as e:
            logger.warning(f"Error reading from cache: {e}")
            return None

    async def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """
        Store a value in the cache.

        Args:
            key: Cache key
            value: Value to store
            ttl: Time-to-live in seconds, or None for no expiration
        """
        cache_path = self._get_cache_path(key)

        try:
            cache_data = {
                "value": value,
                "timestamp": time.time(),
            }

            # Add expiration if TTL is provided
            if ttl is not None:
                cache_data["expiration"] = time.time() + ttl

            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)

            logger.debug(f"Cached value for key: {key}")
        except Exception as e:
            logger.warning(f"Error writing to cache: {e}")

    async def delete(self, key: str) -> bool:
        """
        Delete a value from the cache.

        Args:
            key: Cache key

        Returns:
            True if the value was deleted, False otherwise
        """
        cache_path = self._get_cache_path(key)

        if not cache_path.exists():
            return False

        try:
            cache_path.unlink()
            logger.debug(f"Deleted cache for key: {key}")
            return True
        except Exception as e:
            logger.warning(f"Error deleting from cache: {e}")
            return False

    async def clear(self, older_than: int | None = None) -> int:
        """
        Clear all cache entries or entries older than a specified time.

        Args:
            older_than: Clear only entries older than this many seconds, or None for all

        Returns:
            Number of cache entries cleared
        """
        count = 0

        try:
            for cache_file in self.cache_dir.glob("*.json"):
                try:
                    # If older_than is specified, check the file's modification time
                    if older_than is not None:
                        mtime = cache_file.stat().st_mtime
                        if time.time() - mtime < older_than:
                            continue

                    cache_file.unlink()
                    count += 1
                except Exception as e:
                    logger.warning(f"Error deleting cache file {cache_file}: {e}")

            logger.info(f"Cleared {count} cache entries")
            return count
        except Exception as e:
            logger.warning(f"Error clearing cache: {e}")
            return count

    async def get_stats(self) -> dict[str, Any]:
        """
        Get statistics about the cache.

        Returns:
            Dictionary with cache statistics
        """
        try:
            # Count files and total size
            file_count = 0
            total_size = 0
            oldest_time = time.time()
            newest_time = 0

            for cache_file in self.cache_dir.glob("*.json"):
                file_count += 1
                total_size += cache_file.stat().st_size

                mtime = cache_file.stat().st_mtime
                oldest_time = min(oldest_time, mtime)
                newest_time = max(newest_time, mtime)

            # Convert bytes to human-readable format
            size_str = self._format_size(total_size)

            return {
                "file_count": file_count,
                "total_size": total_size,
                "total_size_formatted": size_str,
                "oldest_entry": None if file_count == 0 else time.ctime(oldest_time),
                "newest_entry": None if file_count == 0 else time.ctime(newest_time),
                "cache_dir": str(self.cache_dir),
            }
        except Exception as e:
            logger.warning(f"Error getting cache stats: {e}")
            return {
                "error": str(e),
                "cache_dir": str(self.cache_dir),
            }

    def _format_size(self, size_bytes: float) -> str:
        """Format a size in bytes to a human-readable string."""
        size_bytes_float = float(size_bytes)  # Convert to float for division
        # Use int for exact byte count if under 1KB
        if size_bytes_float < 1024:
            return f"{int(size_bytes_float)} bytes"
        if size_bytes_float < 1024 * 1024:
            return f"{size_bytes_float / 1024:.1f} KB"
        if size_bytes_float < 1024 * 1024 * 1024:
            return f"{size_bytes_float / (1024 * 1024):.1f} MB"
        return f"{size_bytes_float / (1024 * 1024 * 1024):.1f} GB"

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_git_repository_py_36"></a>

## File: src/repoinsight/git/repository.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 8.3 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.388706 |
| **Type**          | py                         |

```python
"""
Git repository interaction for RepoInsight.

This module provides functionality for interacting with Git repositories,
extracting metadata, and analyzing commits.
"""

import datetime
from pathlib import Path

import git
from git import Repo


class GitRepository:
    """
    Wrapper class for Git repository operations.
    """

    def __init__(self, repo_path: str | Path) -> None:
        """
        Initialize a Git repository wrapper.

        Args:
            repo_path: Path to the Git repository
        """
        self.repo_path = Path(repo_path)
        self._repo: Repo | None = None

    @property
    def repo(self) -> Repo | None:
        """Get the GitPython Repo instance, initializing it if needed."""
        if self._repo is None:
            self._repo = self._initialize_repo()
        return self._repo

    def _initialize_repo(self) -> Repo | None:
        """Initialize and return the GitPython Repo instance."""
        try:
            return Repo(self.repo_path)
        except git.InvalidGitRepositoryError:
            # Not a Git repository, but we'll still provide some basic functionality
            return None

    def is_git_repository(self) -> bool:
        """Check if the path is a valid Git repository."""
        try:
            # Access the repo property to initialize if needed
            _ = self.repo
            return self._repo is not None
        except (git.InvalidGitRepositoryError, git.NoSuchPathError):
            return False

    async def get_metadata(self) -> dict:
        """
        Get repository metadata.

        Returns:
            Dictionary containing repository metadata
        """
        metadata = {
            "path": str(self.repo_path),
            "is_git_repository": self.is_git_repository(),
            "timestamp": datetime.datetime.now().isoformat(),
        }

        # Add Git-specific metadata if available
        if self.is_git_repository():
            try:
                metadata.update(
                    {
                        "active_branch": self.get_active_branch(),
                        "commit_hash": self.get_head_commit_hash(),
                        "commit_message": self.get_head_commit_message(),
                        "commit_date": self.get_head_commit_date(),
                        "author": self.get_head_commit_author(),
                        "remote_urls": self.get_remote_urls(),
                    }
                )
            except Exception as e:
                # Don't fail if some Git operations don't work
                metadata["git_error"] = str(e)

        return metadata

    def get_active_branch(self) -> str:
        """Get the active branch name."""
        if not self.is_git_repository() or self.repo is None:
            return "N/A"

        try:
            return self.repo.active_branch.name
        except (TypeError, ValueError):
            # This can happen in detached HEAD state
            return "HEAD detached"

    def get_head_commit_hash(self) -> str:
        """Get the HEAD commit hash."""
        if not self.is_git_repository() or self.repo is None:
            return "N/A"

        return self.repo.head.commit.hexsha

    def get_head_commit_message(self) -> str:
        """Get the HEAD commit message."""
        if not self.is_git_repository() or self.repo is None:
            return "N/A"

        # Ensure we're returning a string
        message = self.repo.head.commit.message
        return message.strip() if isinstance(message, str) else str(message).strip()

    def get_head_commit_date(self) -> str:
        """Get the HEAD commit date as ISO format string."""
        if not self.is_git_repository() or self.repo is None:
            return "N/A"

        timestamp = self.repo.head.commit.committed_date
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.isoformat()

    def get_head_commit_author(self) -> str:
        """Get the HEAD commit author."""
        if not self.is_git_repository() or self.repo is None:
            return "N/A"

        return f"{self.repo.head.commit.author.name} <{self.repo.head.commit.author.email}>"

    def get_remote_urls(self) -> list[str]:
        """Get a list of remote repository URLs."""
        if not self.is_git_repository() or self.repo is None:
            return []

        return [str(remote.url) for remote in self.repo.remotes]

    def get_file_history(self, file_path: str | Path) -> list[dict]:
        """
        Get the commit history for a specific file.

        Args:
            file_path: Path to the file, relative to repository root

        Returns:
            List of dictionaries containing commit information
        """
        if not self.is_git_repository() or self.repo is None:
            return []

        rel_path = Path(file_path).relative_to(self.repo_path)
        str_path = str(rel_path)

        try:
            # Get commits that modified the file
            commits = list(self.repo.iter_commits(paths=str_path))

            # Format the commit information
            history = []
            for commit in commits:
                history.append(
                    {
                        "hash": commit.hexsha,
                        "short_hash": commit.hexsha[:7],
                        "message": commit.message.strip(),
                        "author": f"{commit.author.name} <{commit.author.email}>",
                        "date": datetime.datetime.fromtimestamp(commit.committed_date).isoformat(),
                    }
                )

            return history
        except Exception:
            # Return empty list if file history cannot be determined
            return []

    def get_file_blame(self, file_path: str | Path) -> list[dict]:
        """
        Get blame information for a specific file.

        Args:
            file_path: Path to the file, relative to repository root

        Returns:
            List of dictionaries containing blame information per line
        """
        if not self.is_git_repository() or self.repo is None:
            return []

        rel_path = Path(file_path).relative_to(self.repo_path)
        str_path = str(rel_path)

        try:
            # Get blame information
            blame = self.repo.git.blame(str_path, "--line-porcelain").split("\n")

            # Parse the blame output
            result: list[dict] = []
            current_commit = None
            current_line = None

            for line in blame:
                if line.startswith("^"):
                    pass  # Boundary commit
                elif line.startswith("\t"):
                    # This is the actual line content
                    if current_commit and current_line:
                        current_commit["content"] = line[1:]  # Remove tab
                        result.append(current_commit)
                        current_commit = None
                        current_line = None
                elif line.startswith("author "):
                    if current_commit:
                        current_commit["author"] = line[7:]
                elif line.startswith("author-time "):
                    if current_commit:
                        timestamp = int(line[12:])
                        dt = datetime.datetime.fromtimestamp(timestamp)
                        current_commit["date"] = dt.isoformat()
                elif line.startswith("summary "):
                    if current_commit:
                        current_commit["summary"] = line[8:]
                elif line.startswith("filename "):
                    if current_commit:
                        current_commit["filename"] = line[9:]
                elif len(line.split()) == 4 and line.split()[0].isalnum():
                    # This should be a commit header line like:
                    # d670460b4b4aece5915caf5c68d12f560a9fe3e4 1 1 1
                    # <sha> <orig-line-no> <final-line-no> <num-lines>
                    parts = line.split()
                    if len(parts[0]) == 40:  # SHA-1 is 40 chars
                        current_commit = {
                            "hash": parts[0],
                            "line_no": parts[2],
                            "line_count": parts[3],
                        }
                        current_line = parts[2]

            return result
        except Exception:
            # Return empty list if blame cannot be determined
            return []

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_git___init___py_37"></a>

## File: src/repoinsight/git/**init**.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 332 bytes                  |
| **Last Modified** | 2025-04-16T16:50:19.028070 |
| **Type**          | py                         |

```python
"""
Git integration package for RepoInsight.

This package provides functionality for interacting with Git repositories
and extracting metadata for documentation.
"""

from repoinsight.git.metadata import GitMetadataExtractor
from repoinsight.git.repository import GitRepository

__all__ = ["GitRepository", "GitMetadataExtractor"]

```

<a id="file__home_mw_Projects_satware_repoinsight_src_repoinsight_git_metadata_py_38"></a>

## File: src/repoinsight/git/metadata.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 6.4 KB                     |
| **Last Modified** | 2025-04-16T19:14:19.030154 |
| **Type**          | py                         |

```python
"""
Git metadata extraction for RepoInsight.

This module handles the extraction and formatting of Git metadata for documentation.
"""

import datetime
from pathlib import Path

from repoinsight.git.repository import GitRepository


class GitMetadataExtractor:
    """
    Extracts formatted metadata from Git repositories for documentation.
    """

    def __init__(self, repository: GitRepository) -> None:
        """
        Initialize a Git metadata extractor.

        Args:
            repository: GitRepository instance to extract metadata from
        """
        self.repository = repository

    async def extract_repository_metadata(self) -> dict:
        """
        Extract comprehensive repository metadata for documentation.

        Returns:
            Dictionary containing formatted repository metadata
        """
        # Get basic metadata from the repository
        metadata = await self.repository.get_metadata()

        # Format the metadata for documentation
        formatted = {
            "Repository Information": {
                "Path": metadata["path"],
                "Git Repository": "Yes" if metadata["is_git_repository"] else "No",
                "Generated": metadata["timestamp"],
            }
        }

        # Add Git-specific information if available
        if metadata.get("is_git_repository"):
            formatted["Git Information"] = {
                "Branch": metadata.get("active_branch", "N/A"),
                "Commit": metadata.get("commit_hash", "N/A"),
                "Commit Message": metadata.get("commit_message", "N/A"),
                "Commit Date": metadata.get("commit_date", "N/A"),
                "Author": metadata.get("author", "N/A"),
            }

            if metadata.get("remote_urls"):
                formatted["Remote Repositories"] = {
                    f"Remote {i+1}": url for i, url in enumerate(metadata.get("remote_urls", []))
                }

        return formatted

    def format_as_markdown(self, metadata: dict) -> str:
        """
        Format the repository metadata as Markdown.

        Args:
            metadata: Repository metadata dictionary from extract_repository_metadata

        Returns:
            Formatted Markdown string
        """
        lines = ["# Repository Metadata\n"]

        for section, data in metadata.items():
            lines.append(f"## {section}\n")

            for key, value in data.items():
                # Handle special cases like lists
                value_str = ", ".join(value) if isinstance(value, list) else str(value)

                lines.append(f"- **{key}:** {value_str}")

            lines.append("")  # Empty line between sections

        return "\n".join(lines)

    async def generate_file_metadata(self, file_path: str | Path) -> dict:
        """
        Generate metadata for a specific file, including Git history if available.

        Args:
            file_path: Path to the file

        Returns:
            Dictionary containing file metadata
        """
        path = Path(file_path)

        # Basic file metadata
        file_metadata = {
            "path": str(path),
            "name": path.name,
            "extension": path.suffix.lstrip(".").lower() if path.suffix else "",
            "size_bytes": path.stat().st_size if path.exists() else 0,
            "last_modified": datetime.datetime.fromtimestamp(
                path.stat().st_mtime if path.exists() else 0
            ).isoformat(),
        }

        # Add Git metadata if available
        if self.repository.is_git_repository():
            try:
                rel_path = path.relative_to(self.repository.repo_path)
                history = self.repository.get_file_history(rel_path)

                if history:
                    file_metadata["git_history"] = {
                        "last_commit": history[0],
                        "commit_count": len(history),
                        "first_commit": history[-1] if len(history) > 0 else None,
                    }
            except (ValueError, Exception):
                # File might be outside repo or other error
                pass

        return file_metadata

    def format_file_metadata_as_markdown(self, metadata: dict) -> str:
        """
        Format file metadata as Markdown.

        Args:
            metadata: File metadata dictionary from generate_file_metadata

        Returns:
            Formatted Markdown string
        """
        lines = [f"# File: {metadata['name']}\n"]

        # Basic metadata
        lines.append("## File Information\n")
        lines.append(f"- **Path:** {metadata['path']}")
        lines.append(f"- **Size:** {self._format_file_size(metadata['size_bytes'])}")
        lines.append(f"- **Last Modified:** {metadata['last_modified']}")
        if metadata.get("extension"):
            lines.append(f"- **Type:** {metadata['extension']}")
        lines.append("")

        # Git history if available
        if "git_history" in metadata:
            history = metadata["git_history"]
            lines.append("## Git History\n")

            if history.get("last_commit"):
                commit = history["last_commit"]
                lines.append("### Latest Commit\n")
                lines.append(f"- **Hash:** {commit['hash']}")
                lines.append(f"- **Date:** {commit['date']}")
                lines.append(f"- **Author:** {commit['author']}")
                lines.append(f"- **Message:** {commit['message']}")
                lines.append("")

            if history.get("commit_count"):
                lines.append(f"- **Total Commits:** {history['commit_count']}")

            if history.get("first_commit"):
                commit = history["first_commit"]
                lines.append("\n### First Commit\n")
                lines.append(f"- **Hash:** {commit['hash']}")
                lines.append(f"- **Date:** {commit['date']}")
                lines.append(f"- **Author:** {commit['author']}")
                lines.append(f"- **Message:** {commit['message']}")

            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def _format_file_size(size_bytes: int) -> str:
        """Format file size in a human-readable way."""
        if size_bytes < 1024:
            return f"{size_bytes} bytes"
        if size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        if size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

```

<a id="file__home_mw_Projects_satware_repoinsight_tests___init___py_39"></a>

## File: tests/**init**.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 39 bytes                   |
| **Last Modified** | 2025-04-16T17:00:05.639943 |
| **Type**          | py                         |

```python
"""
Tests package for RepoInsight.
"""

```

<a id="file__home_mw_Projects_satware_repoinsight_tests_test_config_py_40"></a>

## File: tests/test_config.py

**Language**: python

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 3.4 KB                     |
| **Last Modified** | 2025-04-16T19:04:26.824677 |
| **Type**          | py                         |

```python
"""
Tests for the configuration module.
"""

import tempfile
from pathlib import Path

import pytest
from repoinsight.config.models import FilePatterns, RepoInsightConfig
from repoinsight.config.yaml import ConfigManager, load_config, save_config


def test_file_patterns_defaults() -> None:
    """Test that FilePatterns has the expected defaults."""
    patterns = FilePatterns()
    assert "*.py" in patterns.include
    assert "*.js" in patterns.include
    assert "*.md" in patterns.include
    assert "*__pycache__*" in patterns.exclude
    assert "*.git*" in patterns.exclude


def test_config_required_fields() -> None:
    """Test that RepoInsightConfig requires name and root_path."""
    with pytest.raises(ValueError):
        RepoInsightConfig()  # Missing required fields

    config = RepoInsightConfig(name="Test", root_path="/path/to/repo")
    assert config.name == "Test"
    assert config.root_path == "/path/to/repo"


def test_config_defaults() -> None:
    """Test that RepoInsightConfig has the expected defaults."""
    config = RepoInsightConfig(name="Test", root_path="/path/to/repo")

    assert config.scan_directories == ["."]
    assert "venv" in config.exclude_directories
    assert "node_modules" in config.exclude_directories
    assert ".git" in config.exclude_directories

    assert isinstance(config.file_patterns, FilePatterns)
    assert config.llm.enabled is True
    assert config.llm.provider == "cortex"
    assert config.processing.max_concurrent_tasks == 4
    assert config.output.include_toc is True


def test_save_and_load_config() -> None:
    """Test saving and loading configuration."""
    config = RepoInsightConfig(
        name="Test Config",
        root_path="/test/path",
        output_path="/test/output.md",
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        config_path = Path(temp_dir) / "config.yml"

        # Save config
        save_config(config, config_path)
        assert config_path.exists()

        # Load config
        loaded_config = load_config(config_path)

        # Check that loaded config matches original
        assert loaded_config.name == config.name
        assert loaded_config.root_path == config.root_path
        assert loaded_config.output_path == config.output_path


def test_config_manager() -> None:
    """Test the ConfigManager class."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a ConfigManager with a custom config directory
        config_dir = Path(temp_dir)
        manager = ConfigManager(config_dir)

        # Profiles directory should be created
        profiles_dir = config_dir / "profiles"
        assert profiles_dir.exists()

        # Initially, there should be no profiles
        assert manager.get_available_profiles() == []

        # Create and save a profile
        config = RepoInsightConfig(
            name="Test Profile",
            root_path="/test/profile/path",
        )

        manager.save_profile(config)

        # Should now have one profile
        assert "Test Profile" in manager.get_available_profiles()

        # Load the profile
        loaded_profile = manager.load_profile("Test Profile")
        assert loaded_profile.name == "Test Profile"
        assert loaded_profile.root_path == "/test/profile/path"

        # Delete the profile
        assert manager.delete_profile("Test Profile") is True
        assert "Test Profile" not in manager.get_available_profiles()

```

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_04-security_md_41"></a>

## File: .clinerules/04-security.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 852 bytes                  |
| **Last Modified** | 2025-04-16T18:24:42.133152 |
| **Type**          | md                         |

```markdown
# Security Constraints

- DO NOT access or modify:
  - .env files or secrets directories
  - Private keys or API tokens
  - .pyc or other compiled code
- Sanitize all inputs and outputs to prevent PII leakage
- Treat all scanned code as plain text, NO code execution
- Implement GDPR compliance measures:
  - Detect and redact PII in code, commit messages, and LLM outputs
  - Practice data minimization - only collect necessary information
  - Provide clear user control over data collection and processing
  - Implement appropriate anonymization techniques
- Follow proper input sanitization to prevent injection attacks
- Implement proper open source licensing compliance:
  - Detect licenses of open source code snippets
  - Include appropriate attribution notices
  - Ensure license compatibility
  - Provide clear attribution to original authors
```

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_06-advanced-features_md_42"></a>

## File: .clinerules/06-advanced-features.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.2 KB                     |
| **Last Modified** | 2025-04-16T19:04:26.824015 |
| **Type**          | md                         |

```markdown
# Advanced Features

## Knowledge Graph Construction

- Implement directed graph representation of code relationships
- Track file-to-file dependencies
- Record function and class relationships
- Visualize code structure as navigable graph
- Generate insights based on graph metrics

## Plugin Architecture

- Design abstract plugin interfaces
- Support language-specific plugins for enhanced analysis
- Enable version comparison plugins
- Implement runtime loading of external analysis tools
- Provide comprehensive plugin documentation
- Follow strict security model for plugin isolation

## Multi-Agent Processing

- Coordinate multiple specialized agents
- Implement pipeline stages for code analysis
- Share context efficiently between agents
- Combine insights from specialized agents
- Support plugin-based agent extension
- Handle graceful degradation when specific agents are unavailable

## Advanced LLM Integration

- Support batched processing for efficiency
- Implement fallback mechanism for failed requests
- Fine-tune prompts based on file language and structure
- Cache and reuse similar responses
- Optimize token usage for large repositories
- Provide user-configurable prompt templates
```

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_02-procject-structure_md_43"></a>

## File: .clinerules/02-procject-structure.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.3 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.388669 |
| **Type**          | md                         |

````markdown
# Project Structure

- Root: ~/Projects/satware/repoinsight
- Source code: /src/repoinsight
- Directory structure:

  ```txt
  satware-repoinsight/
  ├── pyproject.toml
  ├── poetry.lock
  ├── README.md
  ├── src/
  │   └── repoinsight/
  │       ├── __init__.py
  │       ├── cli/          # Command-line interface
  │       ├── config/       # Configuration models and handling
  │       ├── git/          # Git repository analysis
  │       ├── scanner/      # File scanning and filtering
  │       ├── llm/          # Language model integration
  │       ├── markdown/     # Document generation
  │       └── gui/          # PySide6 graphical interface
  ├── tests/                # Test suites
  ├── docs/                 # Documentation
  └── scripts/              # Helper scripts
  ```
````

- Exclude directories: venv/, .git/, node_modules/
- Cache folder: /.cache
- Cache organization:
  - File-based by path hash
  - Version control integration with git commit hashes
  - LLM response caching for performance
- Use CommonMark Markdown specification for generated documents
  - Auto-generated Table of Contents
  - Per-file sections with metadata
  - Syntax-highlighted code blocks

````


<a id="file__home_mw_Projects_satware_repoinsight__clinerules_09-cross-agent-collaboration_md_44"></a>

## File: .clinerules/09-cross-agent-collaboration.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property | Value |
| --- | --- |
| **Size** | 2.5 KB |
| **Last Modified** | 2025-04-16T19:04:26.824106 |
| **Type** | md |



```markdown
# Cross-Agent Collaboration

## Integration with Other satware® AI Agents

- Design integration points with specialized satware® AI agents
- Support seamless handoff of context between agents
- Maintain consistent data formats for inter-agent communication
- Implement standardized APIs for agent interaction

## Agent Specializations

- **Tim Alesi (Web Development Expert)**:

  - Optimize PySide6 GUI implementations
  - Enhance UI responsiveness and component design
  - Provide web-standard compliant HTML output for preview

- **Fenix Alesi (Database Expert)**:

  - Optimize caching strategies for repository data
  - Enhance query performance for large repositories
  - Design efficient data structures for code metadata

- **John Alesi (Scientific Research Expert)**:

  - Improve mathematical formalization of code relationships
  - Optimize LLM prompt engineering for technical accuracy
  - Enhance algorithm performance for large-scale analysis

- **Justus Alesi (Legal/Compliance Expert)**:

  - Verify GDPR compliance in scanned repositories
  - Identify license compatibility issues
  - Ensure proper attribution for open source components

- **Luna Alesi (Knowledge Management Expert)**:
  - Enhance organizational knowledge representation
  - Optimize documentation structure for knowledge retention
  - Design metadata schemas for improved searchability

## Collaboration Workflows

- **Sequential Processing**: Chain multiple agents for specialized analysis
- **Parallel Processing**: Distribute work across multiple agents simultaneously
- **Feedback Loops**: Implement iterative improvement through agent feedback
- **Context Sharing**: Maintain shared context to avoid redundant processing
- **Fallback Mechanisms**: Gracefully handle unavailable agent scenarios

## Integration Examples

1. Generate code documentation with RepoInsight → Check for GDPR compliance with Justus Alesi
2. Scan repository structure with RepoInsight → Optimize database queries with Fenix Alesi
3. Create technical documentation with RepoInsight → Enhance knowledge organization with Luna Alesi
4. Document code with RepoInsight → Identify potential bugs with John Alesi
5. Build UI components with RepoInsight → Optimize interface design with Tim Alesi

## Technical Implementation

- Use standardized JSON message formats for agent communication
- Implement versioned API endpoints for agent requests
- Support both synchronous and asynchronous interaction models
- Include detailed metadata in all inter-agent communications
- Log all agent interactions for auditability and debugging

````

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_07-ui-standards_md_45"></a>

## File: .clinerules/07-ui-standards.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.9 KB                     |
| **Last Modified** | 2025-04-16T19:04:26.824056 |
| **Type**          | md                         |

```markdown
# UI Standards and Implementation

## Layout Design

- Follow 3-panel organization (Profiles, Config, Preview)
- Use proper spacing for GUI components (margins, padding)
- Maintain responsive layout that adapts to window resizing
- Implement collapsible panels and sections for complex UIs
- Standardize header, footer, and content area styling
- Use tabs for multi-page content organization

## Component Architecture

- Implement Qt MVC design pattern where appropriate
- Separate UI logic from business logic
- Use signal/slot mechanism for component communication
- Create reusable widgets for common interface elements
- Implement proper widget hierarchy and ownership chain
- Use QSplitter for resizable panel interfaces

## Styling and Appearance

- Use standardized color palette
- Respect system theme when possible
- Implement consistent spacing and alignment
- Use clear visual hierarchy for UI elements
- Apply proper font usage (family, size, weight)
- Maintain accessibility standards for color contrast

## Internationalization (i18n)

- Use Qt Linguist tools for translation management
- Apply tr() function for all user-visible strings
- Support right-to-left languages with proper layout adjustments
- Implement locale-sensitive formatting for dates and numbers
- Store translations in separate resource files
- Test interface with multiple language configurations

## Responsive Design

- Handle window resizing gracefully
- Set minimum window dimensions to prevent UI breakage
- Implement scrollable areas for content overflow
- Use relative sizing (percentages) over fixed pixel values
- Test on varying screen resolutions and DPI settings

## Input Handling

- Validate all user inputs before processing
- Provide clear error feedback for invalid inputs
- Support keyboard navigation and shortcuts
- Implement proper input focus management
- Handle drag and drop operations where appropriate
```

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_01-tech-stack_md_46"></a>

## File: .clinerules/01-tech-stack.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 828 bytes                  |
| **Last Modified** | 2025-04-16T18:23:49.387732 |
| **Type**          | md                         |

```markdown
# Tech Stack

- Python 3.11+ with modern language features (pattern matching, improved error handling, asyncio)
- Poetry for comprehensive dependency management and reproducible builds
- PySide6 for cross-platform GUI with native look and feel
- Compatible with multiple OpenAI-compatible LLM servers:
  - Jan.ai Local API Server
  - vLLM OpenAI-compatible server
  - GPT4All Local API Server
  - LMDeploy RESTful API
  - LocalAI API Server
  - Ollama API integration
- Cross-platform support:
  - Linux (Manjaro/Arch), requires glibc 2.28+
  - Windows 10 (20H2) or newer
  - macOS Catalina (10.15) or newer (Intel and Apple Silicon)
- Minimum system requirements:
  - RAM: 4GB minimum, 8GB+ recommended for large repositories
  - Storage: 500MB for application, plus cache space
  - CPU: Dual-core 2GHz+, quad-core recommended
```

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_05-token-management_md_47"></a>

## File: .clinerules/05-token-management.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.0 KB                     |
| **Last Modified** | 2025-04-16T20:50:50.388706 |
| **Type**          | md                         |

```markdown
# Token Management

- Limit AI context tokens to 75% of model maximum limits
- Prioritize including active context files and metadata
- Cache previous completions for stable repeatability
- Monitor token usage for cost control and efficiency
- Apply compression techniques for large repositories:
  - Truncate file content to relevant portions
  - Summarize lengthy sections when appropriate
  - Use efficient prompt templating
- Implement token budgeting per repository size:

  | Repository Size       | Max Tokens Per File | Max Concurrent Requests |
  | --------------------- | ------------------- | ----------------------- |
  | Small (<100 files)    | 4,000               | 4                       |
  | Medium (<1,000 files) | 2,000               | 8                       |
  | Large (<10,000 files) | 1,000               | 16                      |

- Consider token-efficient representations of code:
  - Focus on API interfaces and signatures
  - Prioritize documentation comments
  - Include relevant imports and dependencies
```

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_03-development-workflow_md_48"></a>

## File: .clinerules/03-development-workflow.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 1.3 KB                     |
| **Last Modified** | 2025-04-16T18:24:25.065598 |
| **Type**          | md                         |

```markdown
# Development Workflow

## Plan Mode

- Generate clear, step-wise implementation plans
- Ask clarifying questions if unclear requirements detected
- Prepare prompts based on file languages and metadata
- Design architecture diagrams when appropriate
- Consider cross-component interactions and dependencies
- Evaluate performance implications for large repositories

## Act Mode

- Apply incremental code changes following user approval
- Insert debug print statements for complex or critical logic
- Monitor linter/compiler errors and fix autonomously when possible
- Use proper error handling and logging throughout the codebase
- Implement comprehensive docstrings and inline comments
- Follow asyncio best practices for concurrent operations:
  - Use semaphores to control concurrency
  - Implement proper exception handling in async tasks
  - Avoid blocking operations in event loops

## Testing Approach

- Write unit tests for core functionality
- Implement integration tests for component interactions
- Add UI tests for PySide6 components
- Create performance benchmarks for different repository sizes
- Follow test-driven development where appropriate

## CI/CD Integration

- Support GitHub Actions workflows
- Enable automatic documentation generation
- Implement semantic versioning for releases
- Include cross-platform build processes
```

<a id="file__home_mw_Projects_satware_repoinsight__clinerules_08-performance-benchmarks_md_49"></a>

## File: .clinerules/08-performance-benchmarks.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 2.0 KB                     |
| **Last Modified** | 2025-04-16T19:04:26.824079 |
| **Type**          | md                         |

```markdown
# Performance Benchmarks and Optimization

## Repository Size Categories

| Repository Size | File Count    | Approximate Lines of Code |
| --------------- | ------------- | ------------------------- |
| Small           | <100 files    | <20,000 LOC               |
| Medium          | <1,000 files  | <200,000 LOC              |
| Large           | <10,000 files | <2,000,000 LOC            |
| Enterprise      | >10,000 files | >2,000,000 LOC            |

## Performance Targets

| Operation              | Small Repo | Medium Repo | Large Repo | Enterprise Repo |
| ---------------------- | ---------- | ----------- | ---------- | --------------- |
| Initial Scan           | <5s        | <30s        | <3m        | <10m            |
| File Filtering         | <1s        | <5s         | <30s       | <2m             |
| LLM Processing (Total) | <2m        | <15m        | <2h        | Custom Planning |
| Markdown Generation    | <3s        | <20s        | <3m        | <15m            |
| Total Process Time     | <3m        | <20m        | <2.5h      | Custom Planning |

## Memory Usage Guidelines

| Repository Size | Peak Memory | Recommended RAM |
| --------------- | ----------- | --------------- |
| Small           | <200MB      | 4GB             |
| Medium          | <500MB      | 8GB             |
| Large           | <1.5GB      | 16GB            |
| Enterprise      | >2GB        | 32GB+           |

## Optimization Strategies

- Implement progressive loading for large repositories
- Apply multi-threading for file scanning and processing
- Control concurrency based on system resources
- Cache intermediate results for interrupted operations
- Support resume functionality for LLM processing
- Use memory-mapped files for large repositories
- Apply adaptive chunking based on file content complexity
- Implement token usage throttling for cost-effective processing
- Offer batch mode for unattended operation on large repositories
- Provide detailed performance metrics and diagnostics
```

<a id="file__home_mw_Projects_satware_repoinsight_docs_USAGE_md_50"></a>

## File: docs/USAGE.md

**Language**: markdown

### Description

Error generating description: Cannot connect to host localhost:8000 ssl:default [Multiple exceptions: [Errno 111] Connect call failed ('::1', 8000, 0, 0), [Errno 111] Connect call failed ('127.0.0.1', 8000)]

### Metadata

| Property          | Value                      |
| ----------------- | -------------------------- |
| **Size**          | 3.7 KB                     |
| **Last Modified** | 2025-04-16T17:35:49.705992 |
| **Type**          | md                         |

````markdown
# satware® RepoInsight User Guide

This guide provides an overview of how to use RepoInsight to document your codebase.

## Basic Usage

RepoInsight can be used in both CLI and GUI modes.

### CLI Mode

```bash
# Basic usage
repoinsight run

# With a specific configuration file
repoinsight run --config sample_config.yml

# With a specific profile
repoinsight run --profile my_profile

# With a specific repository and output path
repoinsight run --repository /path/to/repo --output /path/to/output.md
```
````

### GUI Mode

```bash
# Launch the GUI
repoinsight --gui

# The --gui flag takes precedence over any other command
# and will always launch the GUI regardless of other arguments
```

From the GUI, you can:

1. Open a repository
2. Configure settings
3. Run the documentation generation
4. View and save the output

## Configuration

RepoInsight can be configured using YAML files. You can initialize a default configuration file for your repository:

```bash
repoinsight init /path/to/repo
```

This will create a `.repoinsight.yml` file that you can edit to customize:

- File inclusion/exclusion patterns
- LLM integration settings
- Output formatting options
- And more

See `sample_config.yml` for a comprehensive example.

## Configuration Profiles

You can manage multiple configuration profiles:

```bash
# List available profiles
repoinsight config list

# Create a new profile
repoinsight config create my_profile --repository /path/to/repo

# Delete a profile
repoinsight config delete my_profile
```

## LLM Integration

RepoInsight can use Cortex or other OpenAI-compatible LLM servers to generate descriptions of source code files.

1. Make sure your LLM server is running
2. Configure the `llm` section in your config file
3. Run RepoInsight as usual

### Caching

LLM responses are cached to avoid redundant API calls. You can manage the cache:

```bash
# Show cache info
repoinsight cache info

# Clear the cache
repoinsight cache clear

# Clear only old cache entries
repoinsight cache clear --older-than 30  # 30 days
```

## Programmatic Usage

You can also use RepoInsight programmatically in your Python scripts:

```python
import asyncio
from repoinsight.config.yaml import load_config
from repoinsight.core.engine import ProcessingEngine

async def generate_docs():
    # Load configuration
    config = load_config("sample_config.yml")

    # Create engine
    engine = ProcessingEngine(config)

    # Process repository and generate markdown
    snapshot, markdown = await engine.process_and_generate()

    print(f"Generated documentation with {len(snapshot.files)} files")

    # Save to file if needed
    if config.output_path:
        print(f"Saved to {config.output_path}")

# Run the async function
asyncio.run(generate_docs())
```

See `run_repoinsight.py` for a more detailed example.

## Advanced Topics

### Running with Different LLM Providers

RepoInsight supports various LLM providers through OpenAI-compatible APIs:

1. **Cortex**: Set `llm.provider` to `"cortex"` and configure the API URL
2. **OpenAI**: Set `llm.provider` to `"openai"` and provide your API key
3. **Any OpenAI-compatible API**: Configure the API URL and key accordingly

### Custom Prompts

You can customize the system prompts used to generate file descriptions by editing the `llm.system_prompt_template` in your configuration file.

### Extending RepoInsight

If you want to extend RepoInsight with custom functionality, the modular architecture makes it easy to add new components:

1. Scanner filters: Add new filter implementations in `scanner/filters.py`
2. Prompt templates: Add specialized templates for specific languages in `llm/prompts.py`
3. Markdown components: Add new components in `markdown/components.py`

```




---

Generated at: 2025-04-17T15:23:12.343776
```
