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
