from typing import Dict, Any
from agents.base_agent import BaseAgent
from core.logging import logger

class HRAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="HR Agent",
            description="Checklist and document verification.",
            allowed_tools=["docx", "excel", "document_verification", "checklist"]
        )

    def execute(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        logger.info(f"HRAgent executing task: {task[:50]}...")
        # Simulation
        result_text = f"HR Agent processed policy/employee request: '{task}'."

        return {
            "status": "success",
            "agent": self.name,
            "result": result_text,
            "tools_used": ["docx", "document_verification"]
        }
