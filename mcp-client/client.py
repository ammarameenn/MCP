import asyncio
from typing import *
from contextlib import AsyncExitStack
import requests
import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClient:
    def __init__(self, model_name = "llama3.2"):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.model_name = model_name
        self.ollama_url = "http://localhost:11434/api/generate"
    
    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    # Few consideration to make here:
    # The ollama unlike Anthropic doesn't having native tool calling
    # For example:  in claude there is built in detection like content.type = 'tool_use'
    # Hence we need to simulate this tool calling in ollama.
    async def call_ollama(self, messages: List[Dict[str, str]], tools: Optional[List[Dict]] = None) -> Dict:
        """Make a request to Ollama API"""
        payload = {
            "model": self.ollama_model,
            "messages": messages,
            "stream": False
        }
        
        if tools:
            payload["tools"] = tools
        
        try:
            response = await self.http_client.post(
                f"{self.ollama_base_url}/api/chat",
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error calling Ollama: {e}")
            return {"message": {"content": f"Error: {str(e)}"}}
        
    def format_tools_for_ollama(self, mcp_tools) -> List[Dict]:
        """Convert MCP tools to Ollama tool format"""
        ollama_tools = []
        for tool in mcp_tools:
            ollama_tool = {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description or "",
                    "parameters": tool.inputSchema or {"type": "object", "properties": {}}
                }
            }
            ollama_tools.append(ollama_tool)
        return ollama_tools
    
    def extract_tool_call(self, response_text: str):
        """ Extract tool call from LLM response"""
        lines = response_text.split('\n')
