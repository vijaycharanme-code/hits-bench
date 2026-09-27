from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn

from core.system_state import state
from core.logging import logger
from launcher.system_check import perform_system_check
from orchestration.graph import app_graph

app = FastAPI(title="HITS AI Workbench API")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    decision: Dict[str, Any]

@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI Backend starting up...")
    state.set_status("ONLINE")
    state.backend_ready = True
    # Initial hardware check
    hw = perform_system_check()
    state.update_hardware_info(hw)

@app.get("/health")
def health_check():
    return {"status": state.get_status()}

@app.get("/system")
def get_system_info():
    return state.get_hardware_info()

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    logger.info(f"Received chat request: {request.message[:50]}")

    initial_state = {
        "input": request.message,
        "retry_count": 0
    }

    try:
        # Run LangGraph workflow
        final_state = app_graph.invoke(initial_state)

        return ChatResponse(
            response=final_state.get("final_response", "No response generated."),
            decision=final_state.get("laya_decision", {})
        )
    except Exception as e:
        logger.error(f"Workflow error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
