from pydantic import BaseModel
from typing import Dict, Any


class GraphCreateRequest(BaseModel):
    nodes: Dict[str, str]   # node_name -> python_fn_name
    edges: Dict[str, Any]   # node_name -> next step or branching config


class GraphRunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]
