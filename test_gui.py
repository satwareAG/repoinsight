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
