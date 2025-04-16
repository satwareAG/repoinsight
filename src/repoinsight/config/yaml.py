"""
YAML configuration handling for RepoInsight.

This module provides functionality to load and save configuration files in YAML format,
with proper validation using the Pydantic models.
"""

import os
from pathlib import Path
from typing import Dict, List, Optional, Union

import yaml
from pydantic import ValidationError

from repoinsight.config.models import RepoInsightConfig


def load_config(config_path: Union[str, Path]) -> RepoInsightConfig:
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

    with open(config_path, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)

    try:
        return RepoInsightConfig(**config_data)
    except ValidationError as e:
        # Re-raise with more context
        raise ValidationError(
            f"Invalid configuration in {config_path}: {e.errors()}", e.model
        ) from e


def save_config(config: RepoInsightConfig, config_path: Union[str, Path]) -> None:
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
    directory: Optional[Union[str, Path]] = None,
    config_names: Optional[List[str]] = None,
) -> Optional[Path]:
    """
    Find a configuration file in the specified directory or its parents.
    
    Args:
        directory: Starting directory (defaults to current directory)
        config_names: List of possible config file names (defaults to standard names)
        
    Returns:
        Path to the first found configuration file, or None if not found
    """
    if directory is None:
        directory = Path.cwd()
    else:
        directory = Path(directory)
        
    if config_names is None:
        config_names = [".repoinsight.yml", ".repoinsight.yaml", "repoinsight.yml", "repoinsight.yaml"]
    
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
    
    def __init__(self, config_dir: Optional[Union[str, Path]] = None):
        self.config_dir = Path(config_dir) if config_dir else get_user_config_dir()
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_dir = self.config_dir / "profiles"
        self.profiles_dir.mkdir(exist_ok=True)
        
    def get_available_profiles(self) -> List[str]:
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
    
    def save_profile(self, config: RepoInsightConfig, profile_name: Optional[str] = None) -> None:
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
