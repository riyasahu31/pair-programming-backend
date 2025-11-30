from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import uuid

from backend.db.database import get_db
from backend.models.room import Room
from backend.schemas.room_schema import RoomCreate, RoomResponse

router = APIRouter(
    prefix="/rooms",
    tags=["rooms"]
)

@router.post("/create", response_model=RoomResponse)
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    # Generate unique room_id
    room_id = str(uuid.uuid4())
    new_room = Room(room_id=room_id, code="")
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return RoomResponse(roomId=new_room.room_id)
