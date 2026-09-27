from typing import Dict, Any

def classify_task(user_input: str) -> Dict[str, Any]:
    """
    Simulates Laya's classification logic.
    In a real environment, this would call laya.models or specific fast local classifiers.
    """
    lower_input = user_input.lower()

    # Simple rule-based simulation for the required logic
    if "verify" in lower_input or "check" in lower_input and "document" in lower_input:
        return {
            "task_type": "document_verification",
            "agent": "document_agent",
            "risk": "medium",
            "requires_llm": True
        }
    elif "calculate" in lower_input or "technical" in lower_input or "refinery" in lower_input:
        return {
            "task_type": "technical_analysis",
            "agent": "engineer_agent",
            "risk": "low",
            "requires_llm": True
        }
    elif "report" in lower_input or "summarize" in lower_input:
        return {
            "task_type": "reporting",
            "agent": "supervisor_agent",
            "risk": "low",
            "requires_llm": True
        }
    elif "hr" in lower_input or "employee" in lower_input or "policy" in lower_input:
        return {
            "task_type": "hr_task",
            "agent": "hr_agent",
            "risk": "high",
            "requires_llm": True
        }
    elif "validate answer" in lower_input or "evidence" in lower_input:
        return {
            "task_type": "verification",
            "agent": "verifier_agent",
            "risk": "low",
            "requires_llm": False
        }

    # Default fallback
    return {
        "task_type": "general_inquiry",
        "agent": "supervisor_agent",
        "risk": "low",
        "requires_llm": True
    }
