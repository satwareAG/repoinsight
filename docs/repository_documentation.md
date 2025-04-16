# RepoInsight Project Documentation


## Repository Information

### Repository Information

| Property | Value |
| --- | --- |
| **Path** | /home/mw/Projects/satware/repoinsight |
| **Git Repository** | Yes |
| **Generated** | 2025-04-16T20:48:48.250213 |

### Git Information

| Property | Value |
| --- | --- |
| **Branch** | main |
| **Commit** | 1ee7be0afe9c4f9b1af999d780d4b58a7c5b890a |
| **Commit Message** | Fix mypy type errors in multiple files |
| **Commit Date** | 2025-04-16T18:53:29 |
| **Author** | Michael Wegener <mw@satware.com> |


## Table of Contents

              - [/home/mw/Projects/satware/repoinsight/tests/__init__.py](#file__home_mw_Projects_satware_repoinsight_tests___init___py_0)
              - [/home/mw/Projects/satware/repoinsight/tests/test_config.py](#file__home_mw_Projects_satware_repoinsight_tests_test_config_py_1)


<a id="file__home_mw_Projects_satware_repoinsight_tests___init___py_0"></a>

## File: /home/mw/Projects/satware/repoinsight/tests/__init__.py

**Language**: python

### Description

This is a Python test suite for the `RepoInsight` project, which likely provides insights into repository data. The tests are organized in this package to verify the functionality of `RepoInsight`, ensuring it works as intended across different scenarios and edge cases.

### Metadata

| Property | Value |
| --- | --- |
| **Size** | 39 bytes |
| **Last Modified** | 2025-04-16T17:00:05.639943 |
| **Type** | py |



```python
"""
Tests package for RepoInsight.
"""

```


<a id="file__home_mw_Projects_satware_repoinsight_tests_test_config_py_1"></a>

## File: /home/mw/Projects/satware/repoinsight/tests/test_config.py

**Language**: python

### Description

This code provides unit tests for a configuration module (`repoinsight.config`) that manages settings for a Python project. The tests verify default values, required fields, and functionality of the `ConfigManager` class which handles saving/loading configurations and profile management.

Key patterns used include:
- Using pytest fixtures with temporary directories to isolate test environments
- Testing object initialization and attribute access
- Verifying configuration file persistence through save/load operations
- Implementing profile management logic

### Metadata

| Property | Value |
| --- | --- |
| **Size** | 3.4 KB |
| **Last Modified** | 2025-04-16T19:04:26.824677 |
| **Type** | py |



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




---

Generated at: 2025-04-16T20:48:48.248073
