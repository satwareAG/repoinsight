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
