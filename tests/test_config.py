"""
Tests for the configuration module.
"""

import tempfile
from pathlib import Path

import pytest
from repoinsight.config.models import FilePatterns, RepoInsightConfig
from repoinsight.config.yaml import ConfigManager, load_config, save_config


def test_file_patterns_defaults():
    """Test that FilePatterns has the expected defaults."""
    patterns = FilePatterns()
    assert "*.py" in patterns.include
    assert "*.js" in patterns.include
    assert "*.md" in patterns.include
    assert "*__pycache__*" in patterns.exclude
    assert "*.git*" in patterns.exclude


def test_config_required_fields():
    """Test that RepoInsightConfig requires name and root_path."""
    with pytest.raises(ValueError):
        RepoInsightConfig()  # Missing required fields

    config = RepoInsightConfig(name="Test", root_path="/path/to/repo")
    assert config.name == "Test"
    assert config.root_path == "/path/to/repo"


def test_config_defaults():
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


def test_save_and_load_config():
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


def test_config_manager():
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
