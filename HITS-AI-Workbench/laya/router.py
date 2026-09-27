from typing import Dict, Any, List
from core.logging import logger
from core.exceptions import LayaRoutingError
from laya.classifier import classify_task
from laya.security import check_security

class LayaRouter:
    """
    Laya is the System-1 decision engine.
    Used for task classification, agent routing, tool routing.
    """

    def __init__(self):
        logger.info("Initializing Laya Router...")
        self.ready = True

    def process_request(self, user_input: str) -> Dict[str, Any]:
        """Processes the user request through Laya's System-1 logic."""
        logger.info(f"Laya processing request: {user_input[:50]}...")

        # 1. Security Check
        security_status = check_security(user_input)
        if not security_status["safe"]:
            logger.warning(f"Security check failed: {security_status['reason']}")
            return {
                "safe": False,
                "reason": security_status["reason"],
                "action": "BLOCK"
            }

        # 2. Classification & Routing
        classification = classify_task(user_input)

        # Determine tools based on agent
        tools = self._determine_tools(classification["agent"])

        decision = {
            "safe": True,
            "task_type": classification["task_type"],
            "agent": classification["agent"],
            "tools": tools,
            "risk": classification["risk"],
            "requires_llm": classification.get("requires_llm", True)
        }

        logger.info(f"Laya decision: {decision}")
        return decision

    def _determine_tools(self, agent: str) -> List[str]:
        if agent == "engineer_agent":
            return ["pdf", "ocr", "vision", "rag", "calculator", "reports"]
        elif agent == "supervisor_agent":
            return ["reports", "excel", "checklist", "rag"]
        elif agent == "hr_agent":
            return ["docx", "excel", "document_verification", "checklist"]
        elif agent == "document_agent":
            return ["pdf", "docx", "xlsx", "ocr", "validation"]
        elif agent == "verifier_agent":
            return ["evidence_checking", "consistency_checking", "answer_verification"]
        return []

# Global router instance
router = LayaRouter()
