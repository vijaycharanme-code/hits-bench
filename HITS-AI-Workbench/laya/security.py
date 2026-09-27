from typing import Dict, Any

def check_security(user_input: str) -> Dict[str, Any]:
    """
    Simulates Laya's security checks before execution.
    Checks for prompt injection, malicious instructions.
    """
    lower_input = user_input.lower()

    # Very basic static check simulation
    dangerous_keywords = ["ignore previous instructions", "system prompt", "rm -rf", "drop table"]

    for keyword in dangerous_keywords:
        if keyword in lower_input:
            return {
                "safe": False,
                "reason": f"Detected suspicious instruction related to: {keyword}"
            }

    return {
        "safe": True,
        "reason": "Passed security check"
    }
