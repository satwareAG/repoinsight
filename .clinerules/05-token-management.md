# Token Management

- Limit AI context tokens to 75% of model maximum limits
- Prioritize including active context files and metadata
- Cache previous completions for stable repeatability
- Monitor token usage for cost control and efficiency
- Apply compression techniques for large repositories:
  - Truncate file content to relevant portions
  - Summarize lengthy sections when appropriate
  - Use efficient prompt templating
- Implement token budgeting per repository size:

  | Repository Size       | Max Tokens Per File | Max Concurrent Requests |
  | --------------------- | ------------------- | ----------------------- |
  | Small (<100 files)    | 4,000               | 4                       |
  | Medium (<1,000 files) | 2,000               | 8                       |
  | Large (<10,000 files) | 1,000               | 16                      |

- Consider token-efficient representations of code:
  - Focus on API interfaces and signatures
  - Prioritize documentation comments
  - Include relevant imports and dependencies
