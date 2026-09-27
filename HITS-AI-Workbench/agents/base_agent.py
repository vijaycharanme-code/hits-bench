from abc import ABC, abstractmethod
from typing import List, Dict, Any
from core.logging import logger

class BaseAgent(ABC):
    """Base class for all specific agents."""

    def __init__(self, name: str, description: str, allowed_tools: List[str]):
        self.name = name
        self.description = description
        self.allowed_tools = allowed_tools
        logger.info(f"Initialized {self.name} with tools: {self.allowed_tools}")

    @abstractmethod
    def execute(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Executes the agent's logic for a given task."""
        pass

    def check_tool_allowed(self, tool_name: str) -> bool:
        """Checks if the agent is permitted to use a tool."""
        return tool_name in self.allowed_tools
