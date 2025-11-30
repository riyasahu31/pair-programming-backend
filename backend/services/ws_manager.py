from typing import Dict, List
from fastapi import WebSocket
from backend.db.database import SessionLocal
from backend.models.room import Room

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.setdefault(room_id, []).append(websocket)

    def disconnect(self, room_id: str, websocket: WebSocket):
        if room_id in self.active_connections:
            self.active_connections[room_id].remove(websocket)

    async def broadcast_and_save(self, room_id: str, message: str):
        db = SessionLocal()
        room = db.query(Room).filter(Room.room_id == room_id).first()
        if room:
            room.code = message
            db.commit()
        db.close()

        for connection in self.active_connections.get(room_id, []):
            await connection.send_text(message)

manager = ConnectionManager()
