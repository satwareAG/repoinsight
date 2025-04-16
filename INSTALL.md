# Installation Guide for satware® RepoInsight

This guide provides detailed instructions for installing and setting up RepoInsight on different platforms.

## Prerequisites

- Python 3.11, 3.12, or 3.13
- Git (for repository analysis)
- Cortex or another OpenAI-compatible LLM server (optional, for AI-generated descriptions)

## Option 1: Installation with Poetry (Recommended)

[Poetry](https://python-poetry.org/) is the recommended dependency management tool for RepoInsight.

### 1. Install Poetry

#### Linux/macOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Windows

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 2. Clone the Repository

```bash
git clone https://github.com/satware/repoinsight.git
cd repoinsight
```

### 3. Install Dependencies

```bash
poetry install
```

### 4. Run RepoInsight

```bash
# CLI mode
poetry run repoinsight

# GUI mode
poetry run repoinsight --gui
```

## Option 2: Installation with pip

### 1. Clone the Repository

```bash
git clone https://github.com/satware/repoinsight.git
cd repoinsight
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install RepoInsight in Development Mode

```bash
pip install -e .
```

### 5. Run RepoInsight

```bash
# CLI mode
python -m repoinsight

# GUI mode
python -m repoinsight --gui
```

## Setting Up Cortex for LLM Integration

RepoInsight can use Cortex or other OpenAI-compatible LLM servers to generate descriptions of source code files.

### Running Cortex Locally

1. Install Cortex by following the instructions at <https://cortex.so/docs>

2. Start the Cortex server:

```bash
cortex run llama3
```

3. Configure RepoInsight to use Cortex:
   - Edit your configuration file (e.g., `sample_config.yml`)
   - Ensure `llm.enabled` is set to `true`
   - Set `llm.api_base_url` to your Cortex server URL (default: `http://localhost:8000/v1`)
   - Set `llm.model` to the model you're running (e.g., `llama3`)

## Common Issues and Troubleshooting

### Qt/PySide6 Installation Issues

If you encounter issues installing PySide6, you may need to install additional system dependencies:

#### Ubuntu/Debian

```bash
sudo apt-get install libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xkb1 libxkbcommon-x11-0
```

#### Fedora/RHEL

```bash
sudo dnf install libxcb libxkbcommon-x11
```

#### macOS

```bash
brew install cmake
```

### LLM Integration Issues

If you're having trouble connecting to your LLM server:

1. Verify the server is running and accessible
2. Check your API URL configuration
3. If using Cortex, ensure the model is loaded correctly
4. Try increasing the timeout value in your configuration

## Installing Pre-commit Hooks (for Developers)

```bash
# Install pre-commit
pip install pre-commit

# Install the git hooks
pre-commit install
```
