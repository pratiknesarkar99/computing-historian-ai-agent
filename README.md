# Computing Historian Agent

An interactive chatbot powered by Azure AI that provides information about computing history.

## Overview

This project demonstrates how to interact with a deployed agent on Microsoft Foundry using the Azure AI Projects SDK. The `computing-historian` agent is designed to answer questions about computing history in an interactive conversation format.

## Requirements

- Python 3.8+
- Azure subscription with a Foundry project
- Azure AI Projects SDK

## Installation

1. Install the required dependencies:
   ```bash
   pip install azure-ai-projects>=2.1.0
   ```

2. Ensure you have Azure credentials configured (e.g., via `az login` or environment variables for `DefaultAzureCredential`)

## Configuration

Update the following in `agent.py`:
- `endpoint`: Your Azure AI Foundry project endpoint
- `my_agent`: The agent name (default: "computing-historian")
- `my_version`: The agent version (default: "1")

## Usage

Run the interactive agent:
```bash
python agent.py
```

Enter your prompts at the prompt. The agent will respond with information about computing history. Type `quit` to exit.

Example:
```
Enter a prompt for the agent (or 'quit' to exit): Tell me about the first computer.
Agent response: [response about early computing history]

Enter a prompt for the agent (or 'quit' to exit): quit
Goodbye!
```

## Dependencies

- `azure-identity`: Authentication for Azure services
- `azure-ai-projects`: Azure AI Projects SDK for agent interaction

## License

This project is provided as-is for educational and demonstration purposes.
