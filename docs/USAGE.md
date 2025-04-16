# satware® RepoInsight User Guide

This guide provides an overview of how to use RepoInsight to document your codebase.

## Basic Usage

RepoInsight can be used in both CLI and GUI modes.

### CLI Mode

```bash
# Basic usage
repoinsight run

# With a specific configuration file
repoinsight run --config sample_config.yml

# With a specific profile
repoinsight run --profile my_profile

# With a specific repository and output path
repoinsight run --repository /path/to/repo --output /path/to/output.md
```

### GUI Mode

```bash
# Launch the GUI
repoinsight --gui
```

From the GUI, you can:
1. Open a repository
2. Configure settings
3. Run the documentation generation
4. View and save the output

## Configuration

RepoInsight can be configured using YAML files. You can initialize a default configuration file for your repository:

```bash
repoinsight init /path/to/repo
```

This will create a `.repoinsight.yml` file that you can edit to customize:
- File inclusion/exclusion patterns
- LLM integration settings
- Output formatting options
- And more

See `sample_config.yml` for a comprehensive example.

## Configuration Profiles

You can manage multiple configuration profiles:

```bash
# List available profiles
repoinsight config list

# Create a new profile
repoinsight config create my_profile --repository /path/to/repo

# Delete a profile
repoinsight config delete my_profile
```

## LLM Integration

RepoInsight can use Cortex or other OpenAI-compatible LLM servers to generate descriptions of source code files.

1. Make sure your LLM server is running
2. Configure the `llm` section in your config file
3. Run RepoInsight as usual

### Caching

LLM responses are cached to avoid redundant API calls. You can manage the cache:

```bash
# Show cache info
repoinsight cache info

# Clear the cache
repoinsight cache clear

# Clear only old cache entries
repoinsight cache clear --older-than 30  # 30 days
```

## Programmatic Usage

You can also use RepoInsight programmatically in your Python scripts:

```python
import asyncio
from repoinsight.config.yaml import load_config
from repoinsight.core.engine import ProcessingEngine

async def generate_docs():
    # Load configuration
    config = load_config("sample_config.yml")
    
    # Create engine
    engine = ProcessingEngine(config)
    
    # Process repository and generate markdown
    snapshot, markdown = await engine.process_and_generate()
    
    print(f"Generated documentation with {len(snapshot.files)} files")
    
    # Save to file if needed
    if config.output_path:
        print(f"Saved to {config.output_path}")

# Run the async function
asyncio.run(generate_docs())
```

See `run_repoinsight.py` for a more detailed example.

## Advanced Topics

### Running with Different LLM Providers

RepoInsight supports various LLM providers through OpenAI-compatible APIs:

1. **Cortex**: Set `llm.provider` to `"cortex"` and configure the API URL
2. **OpenAI**: Set `llm.provider` to `"openai"` and provide your API key
3. **Any OpenAI-compatible API**: Configure the API URL and key accordingly

### Custom Prompts

You can customize the system prompts used to generate file descriptions by editing the `llm.system_prompt_template` in your configuration file.

### Extending RepoInsight

If you want to extend RepoInsight with custom functionality, the modular architecture makes it easy to add new components:

1. Scanner filters: Add new filter implementations in `scanner/filters.py`
2. Prompt templates: Add specialized templates for specific languages in `llm/prompts.py`
3. Markdown components: Add new components in `markdown/components.py`
