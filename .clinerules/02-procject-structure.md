# Project Structure

- Root: ~/Projects/satware/repoinsight
- Source code: /src/repoinsight
- Directory structure:
  
  ```txt
  satware-repoinsight/
  ├── pyproject.toml
  ├── poetry.lock
  ├── README.md
  ├── src/
  │   └── repoinsight/
  │       ├── __init__.py
  │       ├── cli/          # Command-line interface
  │       ├── config/       # Configuration models and handling
  │       ├── git/          # Git repository analysis
  │       ├── scanner/      # File scanning and filtering
  │       ├── llm/          # Language model integration
  │       ├── markdown/     # Document generation
  │       └── gui/          # PySide6 graphical interface
  ├── tests/                # Test suites
  ├── docs/                 # Documentation
  └── scripts/              # Helper scripts
  ```

- Exclude directories: venv/, .git/, node_modules/
- Cache folder: /.cache
- Cache organization:
  - File-based by path hash
  - Version control integration with git commit hashes
  - LLM response caching for performance
- Use CommonMark Markdown specification for generated documents
  - Auto-generated Table of Contents
  - Per-file sections with metadata
  - Syntax-highlighted code blocks
