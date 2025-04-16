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
