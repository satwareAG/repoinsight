# satware® RepoInsight

A powerful cross-platform application for automatic documentation of Git repositories with AI-enhanced descriptions.

## Overview

satware® RepoInsight automatically aggregates source code files from any Git repository (or folder structure), combines them into a richly annotated, single markdown document, and enhances this artifact with AI-generated descriptions using an OpenAI-compatible language model API such as Cortex.

## Features

- **Broad Compatibility**: Support for any Git-hosted or local repository; direct folder processing for repos without version control.
- **YAML-Driven Configurability**: Flexible, human-readable configuration format to specify project roots, file inclusion/exclusion rules, output layout, and AI integration parameters.
- **AI-Powered Summarization**: Seamless integration with Cortex or other OpenAI-compatible LLM servers to generate concise, contextually relevant descriptions per file.
- **Rich Metadata Capture**: Embedding of detailed Git repository metadata, including commit hashes, branch names, remote URLs, and generation timestamps.
- **Robust File Scanning**: Efficient, recursive discovery of source files using filters and exclusion rules; accurate language detection for markdown syntax highlighting.
- **Markdown Generation**: Creation of clean, CommonMark-compliant markdown documents with auto-generated Table of Contents, per-file sections, and metadata tags.
- **Cross-Platform GUI**: Modern, intuitive interface built on PySide6, optimized for Linux, Windows, and macOS.
- **Efficient Caching**: Local, filesystem-based caching keyed by file path and repository commit to ensure minimal redundant API calls.

## Installation

### Prerequisites

- Python 3.11 or newer
- Git (for repository analysis)
- Cortex or another OpenAI-compatible LLM server (optional, for AI-generated descriptions)

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/satware/repoinsight.git
cd repoinsight

# Install dependencies with Poetry
poetry install

# Run the application
poetry run repoinsight
```

### Using pip

```bash
# Install from PyPI
pip install repoinsight

# Run the application
repoinsight
```

## Quick Start

1. Launch the application
2. Select a Git repository or folder
3. Configure file inclusion/exclusion patterns
4. Set up LLM integration (optional)
5. Generate the documentation
6. View and export the markdown document

## Configuration

RepoInsight uses YAML configuration files to customize its behavior. Here's a basic example:

```yaml
name: "My Project Documentation"
root_path: "/path/to/repository"
scan_directories:
  - "src"
  - "docs"
exclude_directories:
  - "venv"
  - "node_modules"
  - ".git"
file_patterns:
  include:
    - "*.py"
    - "*.js"
    - "*.md"
  exclude:
    - "*.pyc"
    - "*.min.js"
llm:
  enabled: true
  api_base_url: "http://localhost:8000/v1"
  model: "llama3"
  temperature: 0.3
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
