from typing import Dict, Any
from agents.base_agent import BaseAgent
from core.logging import logger

class DocumentAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Document Agent",
            description="OCR + validation.",
            allowed_tools=["pdf", "docx", "xlsx", "ocr", "validation"]
        )

    def execute(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        logger.info(f"DocumentAgent executing task: {task[:50]}...")
        # Simulation
        result_text = f"Document Agent extracted and validated info for: '{task}'."

        return {
            "status": "success",
            "agent": self.name,
            "result": result_text,
            "tools_used": ["pdf", "ocr", "validation"]
        }
