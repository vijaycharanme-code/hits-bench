import pytest
from agents.engineer_agent import EngineerAgent

def test_engineer_agent():
    agent = EngineerAgent()
    assert "calculator" in agent.allowed_tools

    res = agent.execute("calculate this value")
    assert res["status"] == "success"
    assert "calculator" in res["tools_used"]
