from typing import Dict, Any
from agents.base_agent import BaseAgent
from core.logging import logger

class SupervisorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Supervisor Agent",
            description="Reports and summaries.",
            allowed_tools=["reports", "excel", "checklist", "rag"]
        )

    def execute(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        logger.info(f"SupervisorAgent executing task: {task[:50]}...")
        # Simulation
        result_text = f"Supervisor Agent generated a report/summary for: '{task}'."

        return {
            "status": "success",
            "agent": self.name,
            "result": result_text,
            "tools_used": ["reports"]
        }
