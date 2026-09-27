from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List, Dict, Any
import operator
from laya.router import router as laya_router
from orchestration.planner import plan_execution
from orchestration.executor import execute_plan
from orchestration.verifier import verify_execution
from orchestration.correction import correct_execution

class WorkflowState(TypedDict):
    input: str
    laya_decision: Dict[str, Any]
    plan: List[str]
    execution_results: List[Dict[str, Any]]
    verification_passed: bool
    retry_count: int
    final_response: str
    error: str

def route_request(state: WorkflowState):
    decision = laya_router.process_request(state["input"])
    return {"laya_decision": decision}

def generate_plan(state: WorkflowState):
    if not state["laya_decision"]["safe"]:
        return {"plan": [], "error": state["laya_decision"]["reason"]}
    plan = plan_execution(state["input"], state["laya_decision"])
    return {"plan": plan, "retry_count": state.get("retry_count", 0)}

def execute(state: WorkflowState):
    if state.get("error"):
        return {"execution_results": []}
    results = execute_plan(state["plan"], state["laya_decision"])
    return {"execution_results": results}

def verify(state: WorkflowState):
    if state.get("error"):
        return {"verification_passed": False, "final_response": f"Blocked: {state['error']}"}
    passed, response = verify_execution(state["execution_results"], state["laya_decision"])
    return {"verification_passed": passed, "final_response": response}

def check_verification(state: WorkflowState):
    if state.get("error"):
        return END
    if state["verification_passed"]:
        return END
    if state["retry_count"] >= 3:
        return END
    return "correct"

def correct(state: WorkflowState):
    new_plan = correct_execution(state["plan"], state["execution_results"])
    return {"plan": new_plan, "retry_count": state["retry_count"] + 1}

def build_graph():
    workflow = StateGraph(WorkflowState)

    workflow.add_node("route", route_request)
    workflow.add_node("plan", generate_plan)
    workflow.add_node("execute", execute)
    workflow.add_node("verify", verify)
    workflow.add_node("correct", correct)

    workflow.set_entry_point("route")
    workflow.add_edge("route", "plan")
    workflow.add_edge("plan", "execute")
    workflow.add_edge("execute", "verify")

    workflow.add_conditional_edges(
        "verify",
        check_verification,
        {
            END: END,
            "correct": "correct"
        }
    )

    workflow.add_edge("correct", "execute")

    return workflow.compile()

app_graph = build_graph()
