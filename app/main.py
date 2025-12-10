from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import Dict, Any
from uuid import uuid4

from app.engine.graph_engine import GraphRunner
from app.websocket_manager import (
    connect_websocket,
    disconnect_websocket,
    broadcast_log
)

from app.workflows.code_review import (
    extract_functions,
    check_complexity,
    detect_issues,
    suggest_improvements,
    should_loop
)

app = FastAPI()
runner = GraphRunner()


class GraphRequest(BaseModel):
    nodes: Dict[str, str]
    edges: Dict[str, Any]


class RunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]


@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await connect_websocket(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await disconnect_websocket(websocket)


@app.post("/graph/create")
def create_graph(req: GraphRequest):
    node_map = {
        "extract_functions": extract_functions,
        "check_complexity": check_complexity,
        "detect_issues": detect_issues,
        "suggest_improvements": suggest_improvements,
        "should_loop": should_loop
    }

    nodes = {key: node_map[value] for key, value in req.nodes.items()}
    graph_id = runner.create_graph(nodes, req.edges)
    return {"graph_id": graph_id}


@app.post("/graph/run")
async def run_graph(req: RunRequest):
    run_id, final_state, log = await runner.run_graph(req.graph_id, req.initial_state)
    return {
        "run_id": run_id,
        "final_state": final_state,
        "execution_log": log
    }


@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    return runner.get_run_state(run_id)
