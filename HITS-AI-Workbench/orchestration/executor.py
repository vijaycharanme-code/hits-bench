from typing import Dict, Any, List
from core.logging import logger
from agents.engineer_agent import EngineerAgent
from agents.supervisor_agent import SupervisorAgent
from agents.hr_agent import HRAgent
from agents.document_agent import DocumentAgent
from agents.verifier_agent import VerifierAgent

def execute_plan(plan: List[str], decision: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Executes the plan using the selected agent."""
    agent_name = decision["agent"]
    logger.info(f"Executing plan with agent: {agent_name}")

    agent = None
    if agent_name == "engineer_agent":
        agent = EngineerAgent()
    elif agent_name == "supervisor_agent":
        agent = SupervisorAgent()
    elif agent_name == "hr_agent":
        agent = HRAgent()
    elif agent_name == "document_agent":
        agent = DocumentAgent()
    elif agent_name == "verifier_agent":
        agent = VerifierAgent()
    else:
        agent = SupervisorAgent() # default

    results = []
    for step in plan:
        res = agent.execute(step)
        results.append(res)

    return results
