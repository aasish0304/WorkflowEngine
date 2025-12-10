import uuid
import asyncio
from typing import Callable, Dict, Any
from app.websocket_manager import broadcast_log


class WorkflowGraph:
    def __init__(self, nodes: Dict[str, Callable], edges: Dict[str, Any]):
        self.nodes = nodes
        self.edges = edges


class GraphRunner:
    def __init__(self):
        self.graphs = {}
        self.runs = {}

    def create_graph(self, nodes, edges):
        graph_id = str(uuid.uuid4())
        graph = WorkflowGraph(nodes, edges)
        self.graphs[graph_id] = graph
        return graph_id

    async def run_graph(self, graph_id, initial_state):
        run_id = str(uuid.uuid4())
        graph = self.graphs[graph_id]

        state = initial_state.copy()
        log = []

        current_node = list(graph.nodes.keys())[0]

        while current_node is not None:
            fn = graph.nodes[current_node]
            result = fn(state)
            state.update(result)

            log_entry = {"node": current_node, "state": state.copy()}
            log.append(log_entry)

            await broadcast_log(log_entry)
            await asyncio.sleep(0)

            edge = graph.edges.get(current_node)

            if isinstance(edge, dict) and "condition" in edge:
                condition_fn = graph.nodes[edge["condition"]]
                if condition_fn(state):
                    current_node = edge["true"]
                else:
                    current_node = edge["false"]
            else:
                current_node = edge

        self.runs[run_id] = {"final_state": state, "log": log}
        return run_id, state, log

    def get_run_state(self, run_id):
        return self.runs.get(run_id)
