from typing import Dict, Any, List, Tuple
from core.logging import logger

def verify_execution(results: List[Dict[str, Any]], decision: Dict[str, Any]) -> Tuple[bool, str]:
    """Verifies if the execution results meet the requirements."""
    logger.info("Verifying execution results...")

    if not results:
        return False, "No results generated."

    # Simulate a verification failure randomly or based on condition (here always pass for sim)
    final_text = " ".join([r.get("result", "") for r in results])
    return True, f"Final Answer: {final_text}"
