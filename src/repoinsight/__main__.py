"""
Main entry point for RepoInsight.

This module provides the main entry point for the application,
allowing users to choose between the CLI and GUI interfaces.
"""

import logging
import sys
from typing import List, Optional

from repoinsight import __version__
from repoinsight.cli.commands import app as cli_app
from repoinsight.gui.app import run_app as run_gui


def main(args: Optional[List[str]] = None) -> int:
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
    
    # Use provided args or sys.argv
    if args is None:
        args = sys.argv[1:]
        
    # Check for special "--gui" flag
    if "--gui" in args:
        # Remove the flag from args
        args.remove("--gui")
        
        # If there are still arguments, print a warning
        if args:
            print("Warning: Additional arguments are ignored in GUI mode.")
            
        # Run the GUI
        return run_gui()
    else:
        # Run the CLI with the remaining arguments
        return cli_app()


if __name__ == "__main__":
    sys.exit(main())
