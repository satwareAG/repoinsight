# Security Constraints

- DO NOT access or modify:
  - .env files or secrets directories
  - Private keys or API tokens
  - .pyc or other compiled code
- Sanitize all inputs and outputs to prevent PII leakage
- Treat all scanned code as plain text, NO code execution
- Implement GDPR compliance measures:
  - Detect and redact PII in code, commit messages, and LLM outputs
  - Practice data minimization - only collect necessary information
  - Provide clear user control over data collection and processing
  - Implement appropriate anonymization techniques
- Follow proper input sanitization to prevent injection attacks
- Implement proper open source licensing compliance:
  - Detect licenses of open source code snippets
  - Include appropriate attribution notices
  - Ensure license compatibility
  - Provide clear attribution to original authors
