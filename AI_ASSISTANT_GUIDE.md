# Browser-Use Setup and Usage Guide for AI Assistants

This guide provides instructions for setting up and using the browser-use library, which enables AI agents to interact with web browsers.

## Setup Process

### 1. Environment Setup

The browser-use library requires API keys for language models. The following steps outline how to set up the environment:

1. Create or modify the `.env` file in the project root directory with the appropriate API keys:

```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
AZURE_ENDPOINT=your_azure_endpoint
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
DEEPSEEK_API_KEY=your_deepseek_api_key

# Set to false to disable anonymized telemetry
ANONYMIZED_TELEMETRY=true

# LogLevel: Set to debug to enable verbose logging, set to result to get results only. Available: result | debug | info
BROWSER_USE_LOGGING_LEVEL=info

# set this to true to optimize browser-use's chrome for running inside docker
IN_DOCKER=false
```

2. Ensure you have at least one of the following API keys set:
   - OPENAI_API_KEY (for OpenAI models)
   - ANTHROPIC_API_KEY (for Anthropic Claude models)
   - GEMINI_API_KEY (for Google Gemini models)
   - DEEPSEEK_API_KEY (for Deepseek models)

3. Activate the virtual environment before running any examples:
   ```
   source .venv/bin/activate
   ```

### 2. Dependency Management

If you need to install additional dependencies, use the following command with the virtual environment activated:

```
uv pip install package_name
```

Note: Using `pip install` directly may result in an "externally-managed-environment" error.

## Running Examples

The browser-use repository contains various examples demonstrating different capabilities:

### Basic Example

To run the basic example:

```
source .venv/bin/activate && python examples/simple.py
```

This example demonstrates how to:
- Initialize a language model (OpenAI's GPT-4o)
- Create an Agent with a specific task
- Run the agent to complete the task

### Use Case Examples

The repository includes several use case examples in the `examples/use-cases/` directory:

1. **Scrolling Page Example**:
   ```
   source .venv/bin/activate && python examples/use-cases/scrolling_page.py
   ```
   This example demonstrates how to navigate to a webpage and scroll to find specific text.

2. **Wikipedia Navigation**:
   ```
   source .venv/bin/activate && python examples/use-cases/wikipedia_banana_to_quantum.py
   ```
   This example shows how to navigate from one Wikipedia page to another by clicking on links.

3. Other use cases include:
   - CAPTCHA solving
   - Appointment checking
   - Job application automation
   - Online coding
   - Social media posting
   - Web voyager agent

## Model-Specific Examples

The repository includes examples for different language models in the `examples/models/` directory:

1. **OpenAI Models**:
   ```
   source .venv/bin/activate && python examples/models/gpt-4o.py
   ```

2. **Anthropic Claude Models**:
   ```
   source .venv/bin/activate && python examples/models/claude-3.7-sonnet.py
   ```

3. **Other Models**:
   - Deepseek
   - Gemini
   - Azure OpenAI
   - Bedrock Claude
   - Ollama
   - Qwen

## Troubleshooting

### Common Issues

1. **Environment Variables Not Set**:
   - Ensure the appropriate API key is set in the `.env` file
   - The Agent checks for required environment variables based on the LLM class name
   - For example, `ChatOpenAI` requires `OPENAI_API_KEY`

2. **Rate Limit Errors**:
   - If you encounter rate limit errors, try using a different model or wait before retrying

3. **Model-Specific Issues**:
   - Some models may have specific requirements or limitations
   - Refer to the model-specific examples for guidance

## Key Concepts

### Agent

The `Agent` class is the main interface for interacting with the browser. It takes the following parameters:

- `task`: The task to be performed
- `llm`: The language model to use
- `browser`: (Optional) A custom browser configuration
- `use_vision`: (Optional) Whether to use vision capabilities
- `max_failures`: (Optional) Maximum number of consecutive failures before stopping
- `max_actions_per_step`: (Optional) Maximum number of actions per step

### Browser

The `Browser` class represents the browser instance. It can be configured with:

- `BrowserConfig`: Configuration for the browser
- `BrowserContextConfig`: Configuration for the browser context

### Actions

The agent can perform various actions:

- `go_to_url`: Navigate to a URL
- `click_element_by_index`: Click on an element
- `input_text`: Type text into an input field
- `scroll_down`: Scroll down the page
- `scroll_up`: Scroll up the page
- `scroll_to_text`: Scroll to specific text
- `extract_content`: Extract content from the page
- `done`: Complete the task

## Advanced Features

The browser-use library includes advanced features such as:

- Custom system prompts
- Custom output formats
- Multi-tab handling
- Parallel agents
- Result processing
- Sensitive data handling
- Custom functions

Refer to the examples in the `examples/features/` directory for more information.