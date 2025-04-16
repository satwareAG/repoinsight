# Development Workflow

## Plan Mode

- Generate clear, step-wise implementation plans
- Ask clarifying questions if unclear requirements detected
- Prepare prompts based on file languages and metadata
- Design architecture diagrams when appropriate
- Consider cross-component interactions and dependencies
- Evaluate performance implications for large repositories

## Act Mode

- Apply incremental code changes following user approval
- Insert debug print statements for complex or critical logic
- Monitor linter/compiler errors and fix autonomously when possible
- Use proper error handling and logging throughout the codebase
- Implement comprehensive docstrings and inline comments
- Follow asyncio best practices for concurrent operations:
  - Use semaphores to control concurrency
  - Implement proper exception handling in async tasks
  - Avoid blocking operations in event loops

## Testing Approach

- Write unit tests for core functionality
- Implement integration tests for component interactions
- Add UI tests for PySide6 components
- Create performance benchmarks for different repository sizes
- Follow test-driven development where appropriate

## CI/CD Integration

- Support GitHub Actions workflows
- Enable automatic documentation generation
- Implement semantic versioning for releases
- Include cross-platform build processes
