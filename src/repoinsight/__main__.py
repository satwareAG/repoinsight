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
