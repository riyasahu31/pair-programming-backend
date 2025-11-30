from pydantic import BaseModel

class RoomCreate(BaseModel):
    pass  # No input needed to create room

class RoomResponse(BaseModel):
    roomId: str

class AutocompleteRequest(BaseModel):
    code: str
    cursorPosition: int
    language: str

class AutocompleteResponse(BaseModel):
    suggestion: str
