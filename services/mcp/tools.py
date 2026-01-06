"""Simple MCP tools implementation."""

from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Demo MCP Server")


@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name.

    Args:
        name: The name of the person to greet

    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to FastMCP demo."


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


@mcp.tool()
def get_server_info() -> dict:
    """Get information about the MCP server.

    Returns:
        A dictionary containing server information
    """
    return {
        "name": "Demo MCP Server",
        "version": "1.0.0",
        "tools_count": 3,
        "description": "A simple MCP server with basic tools",
    }
