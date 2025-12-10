from fastapi import WebSocket, WebSocketDisconnect
from typing import List

active_connections: List[WebSocket] = []

async def connect_websocket(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

async def disconnect_websocket(websocket: WebSocket):
    active_connections.remove(websocket)

async def broadcast_log(message: dict):
    for ws in list(active_connections):
        try:
            await ws.send_json(message)
        except WebSocketDisconnect:
            active_connections.remove(ws)
