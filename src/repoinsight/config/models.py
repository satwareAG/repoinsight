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
            "Analyze the following {language} code and provide a concise description in markdown format. "
            "Focus on the main purpose, key functionality, and important patterns or techniques used. "
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
