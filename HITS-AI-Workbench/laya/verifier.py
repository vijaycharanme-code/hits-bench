from typing import Dict, Any

def verify_tool_request(tool_name: str, args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Checks if a tool request is valid and safe.
    """
    if tool_name == "filesystem":
        # Ensure we're not accessing sensitive paths
        path = args.get("path", "")
        if ".." in path or path.startswith("/etc") or path.startswith("C:\\Windows"):
            return {
                "safe": False,
                "reason": "Unsafe filesystem access"
            }

    return {
        "safe": True,
        "reason": "Tool request is safe"
    }
