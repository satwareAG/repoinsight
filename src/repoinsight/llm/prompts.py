"""
System prompt templates for LLM interactions.

This module provides specialized system prompts for various programming languages
and file types to improve the quality of generated descriptions.
"""


class PromptTemplates:
    """
    Collection of system prompt templates for different programming languages and file types.
    """

    # Default prompt template for any language
    DEFAULT_TEMPLATE = (
        "Analyze the following {language} code and provide a concise description "
        "in markdown format. Focus on the main purpose, key functionality, and "
        "important patterns or techniques used. Keep the description under 5 sentences. "
        "Use technical but clear language appropriate for a software documentation context."
    )

    # Specialized templates for specific languages
    LANGUAGE_TEMPLATES = {
        # Python-specific prompt
        "python": (
            "Analyze the following Python code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The module's main purpose and functionality\n"
            "2. Key classes, functions, and their relationships\n"
            "3. Important design patterns or Python idioms used\n"
            "4. Dependencies and their roles\n"
            "5. Any notable algorithms or techniques\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for Python developers. If appropriate, mention Python-specific "
            "features like decorators, context managers, generators, or async functionality."
        ),
        # JavaScript/TypeScript prompt
        "javascript": (
            "Analyze the following JavaScript code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The module's main purpose and functionality\n"
            "2. Key functions, classes, or components\n"
            "3. Important design patterns or JavaScript idioms used\n"
            "4. Dependencies and their roles\n"
            "5. Any notable frameworks or libraries used\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for JavaScript developers. If appropriate, mention JavaScript-specific "
            "features like closures, promises, async/await, or functional patterns."
        ),
        "typescript": (
            "Analyze the following TypeScript code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The module's main purpose and functionality\n"
            "2. Key interfaces, types, classes, or components\n"
            "3. Important design patterns or TypeScript idioms used\n"
            "4. Type system features being leveraged\n"
            "5. Any notable frameworks or libraries used\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for TypeScript developers. If appropriate, mention TypeScript-specific "
            "features like generics, type guards, utility types, or advanced type constructs."
        ),
        # HTML/CSS prompt
        "html": (
            "Analyze the following HTML code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The document's main purpose and structure\n"
            "2. Key sections, components, or elements\n"
            "3. Important accessibility features\n"
            "4. Integration with other technologies (CSS, JavaScript)\n"
            "5. Any notable frameworks or libraries used\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for web developers."
        ),
        "css": (
            "Analyze the following CSS code and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The stylesheet's main purpose and scope\n"
            "2. Key styling patterns or component styles\n"
            "3. Important CSS techniques or methodologies used (e.g., Flexbox, Grid, BEM)\n"
            "4. Responsive design approaches\n"
            "5. Any notable preprocessor features (if using SCSS/LESS)\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for web developers."
        ),
        # Configuration files prompt
        "json": (
            "Analyze the following JSON configuration file and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The configuration's main purpose\n"
            "2. Key sections or settings\n"
            "3. Important options and their significance\n"
            "4. How this configuration relates to the application\n"
            "5. Any notable patterns or structures\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "that explains the purpose and key aspects of this configuration."
        ),
        "yaml": (
            "Analyze the following YAML configuration file and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The configuration's main purpose\n"
            "2. Key sections or settings\n"
            "3. Important options and their significance\n"
            "4. How this configuration relates to the application\n"
            "5. Any notable patterns or structures\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "that explains the purpose and key aspects of this configuration."
        ),
        "toml": (
            "Analyze the following TOML configuration file and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The configuration's main purpose\n"
            "2. Key sections or settings\n"
            "3. Important options and their significance\n"
            "4. How this configuration relates to the application\n"
            "5. Any notable patterns or structures\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "that explains the purpose and key aspects of this configuration."
        ),
        # Documentation files prompt
        "markdown": (
            "Analyze the following Markdown document and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The document's main purpose and topic\n"
            "2. Key sections or headings\n"
            "3. Important information or instructions contained\n"
            "4. The target audience\n"
            "5. Any notable formatting or structure\n\n"
            "Keep the description under 5 sentences. Provide a clear summary that captures "
            "the essence and purpose of this documentation."
        ),
        # Shell scripts prompt
        "bash": (
            "Analyze the following shell script and provide a concise description "
            "in markdown format. Focus on:\n"
            "1. The script's main purpose and functionality\n"
            "2. Key commands or operations performed\n"
            "3. Important parameters or environment variables used\n"
            "4. Error handling or validation mechanisms\n"
            "5. Any notable shell-specific techniques\n\n"
            "Keep the description under 5 sentences. Use technical but clear language "
            "appropriate for system administrators or DevOps engineers."
        ),
    }

    @classmethod
    def get_template(cls, language: str) -> str:
        """
        Get a prompt template for a specific language.

        Args:
            language: The programming language or file type

        Returns:
            A prompt template string with a {language} placeholder
        """
        # Normalize the language name
        norm_language = language.lower()

        # Check for direct language match
        if norm_language in cls.LANGUAGE_TEMPLATES:
            return cls.LANGUAGE_TEMPLATES[norm_language]

        # Check for language aliases
        if norm_language in ["js", "jsx"]:
            return cls.LANGUAGE_TEMPLATES["javascript"]
        if norm_language in ["ts", "tsx"]:
            return cls.LANGUAGE_TEMPLATES["typescript"]
        if norm_language in ["py"]:
            return cls.LANGUAGE_TEMPLATES["python"]
        if norm_language in ["scss", "less"]:
            return cls.LANGUAGE_TEMPLATES["css"]
        if norm_language in ["yml"]:
            return cls.LANGUAGE_TEMPLATES["yaml"]
        if norm_language in ["sh", "shell", "zsh"]:
            return cls.LANGUAGE_TEMPLATES["bash"]
        if norm_language in ["md"]:
            return cls.LANGUAGE_TEMPLATES["markdown"]

        # Fallback to default template
        return cls.DEFAULT_TEMPLATE


def get_system_prompt(language: str) -> str:
    """
    Get a formatted system prompt for a specific language.

    Args:
        language: The programming language or file type

    Returns:
        A formatted system prompt
    """
    template = PromptTemplates.get_template(language)
    return template.format(language=language)
