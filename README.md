# MCP Demo: Self-Hosted AI Pipeline for Privacy-First Applications

A demonstration of how Model Context Protocol (MCP) enables secure, self-hosted AI services that keep sensitive data within trusted environments. This weather service demo showcases the architectural patterns needed for privacy-critical applications like Rider Spoke.

## 🎯 Core Demonstration

This project proves the viability of self-hosted AI pipelines by:

- Running local LLMs (Llama 3.2, Falcon3) without external API dependencies
- Implementing secure tool integration via MCP protocol
- Processing real-time data while maintaining privacy boundaries
- Demonstrating modular, API-driven architecture suitable for creative applications

## 🏗️ Architecture: Privacy-First AI Services
![MCP Architecture](MCP.drawio.png)

### Key Privacy Principles Demonstrated:

- ✅ No data leaves local environment
- ✅ Self-hosted models with full control
- ✅ Modular tool architecture for easy extension
- ✅ Secure internal APIs only

### 🎯 Current functionality
This project showcases how MCP enables seamless integration between Large Language Models and external APIs. The demo consists of:

- **MCP Server**: Exposes weather tools (alerts & forecasts) via standardized MCP protocol
- **LLM Client**: Uses PraisonAI Agents with local Ollama models to interact with weather tools
- **Real-time Data**: Fetches live weather information from the US National Weather Service

### Get started: Prerequisites
#### System Requirements

- Linux Operating System (Ollama is optimized for Linux environments)
- Python 3.8 or higher
- Git (for cloning the repository)

#### Ollama Installation

```bash
# Before running this project, you need to install Ollama on your Linux system:
curl -fsSL https://ollama.com/install.sh | sh
```
Alternatively, you can download and install Ollama manually from [ollama.com](https://ollama.com/download/linux)

#### Verify Ollama Installation
```bash
ollama --version
```

### 📋 Example Interactions
#### Weather Alerts Query
```
🧑 You: Check weather alerts for Florida
🤖 Agent: I'll check the current weather alerts for Florida.

Current active alerts for FL:

Event: Hurricane Warning
Area: Southeast Florida
Severity: Extreme
Description: Hurricane conditions expected within 36 hours...
Instructions: Complete preparations immediately...
Forecast Query

🧑 You: What's the weather forecast for San Francisco? (37.7749, -122.4194)
🤖 Agent: Here's the 5-day forecast for San Francisco:

Tonight:
Temperature: 58°F
Wind: 10 mph W
Forecast: Partly cloudy with patchy fog developing after midnight...
```