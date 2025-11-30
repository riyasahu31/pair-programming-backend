from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from backend.db.init_db import init_db
from backend.routers.rooms import router as rooms_router
from backend.routers.autocomplete import router as autocomplete_router
from backend.services.ws_manager import manager
from backend.db.database import SessionLocal
from backend.models.room import Room

app = FastAPI(title="Pair Programming Backend")

@app.on_event("startup")
def on_startup():
    init_db()

# Include routers
app.include_router(rooms_router)
app.include_router(autocomplete_router)

# Home route
@app.get("/")
def home():
    return {"message": "Backend is running"}

# WebSocket endpoint
@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(room_id, websocket)

    # Send existing code to new client
    db = SessionLocal()
    room = db.query(Room).filter(Room.room_id == room_id).first()
    if room and room.code:
        await websocket.send_text(room.code)
    db.close()

    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast_and_save(room_id, data)
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
