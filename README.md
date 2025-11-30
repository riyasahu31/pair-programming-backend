# PAIR PROGRAMMING PROTOTYPE - BACKEND

## Overview:

This is a simplified real-time pair-programming backend built with **FastAPI** and **WebSockets**.
Two users can join the same room, edit code collaboratively, and see each other's changes instantly.
A mocked AI-style autocomplete is also provided.

## Tech Stack:

**Backend**: Python 3.12, FastAPI, WebSockets, PostgreSQL
**Database ORM**: SQLAlchemy

## Features:

1. **Room Management**
   - Create a new room: `POST /rooms/create` → returns `roomId`
   - Join an existing room via WebSocket: `/ws/{room_id}` WebSocket syncs code between users

2. **Real-Time Collaborative Coding**
   - WebSocket syncs code in real-time between users in the same room.
   - Last-write-wins approach for simplicity.
   - Room code persisted in PostgreSQL.

3. **AI Autocomplete (Mocked)**
   - `POST /autocomplete`
   - Accepts: { code, cursorPosition, language }
   - Returns a mocked suggestion: `{ suggestion: "..." }`

## Setup & Run:

1. Clone the repo
2. Create virtual environment:
   python -m venv .venv
3. Activate venv:
   source .venv/bin/activate   (Linux/Mac)
   .venv\Scripts\activate      (Windows)
4. Install dependencies:
   pip install -r requirements.txt
5. Set environment variables in .env:
   DB_USER=pairuser
   DB_PASS=pairpass
   DB_HOST=localhost
   DB_NAME=pair_programming
6. Start backend:
   uvicorn backend.main:app --reload
7. API available at:
   `http://127.0.0.1:8000`

## Testing:

- Use Postman or a browser WebSocket client.
- Create a room: `POST /rooms/create` → returns roomId
- Connect two clients via WebSocket: `ws://127.0.0.1:8000/ws/{roomId}`
- Test autocomplete: `POST /autocomplete`

## Design Choices & Notes:

- WebSocket manager handles multiple rooms and client connections.
- Last-write-wins approach for real-time code sync.
- Autocomplete is mocked; can be replaced with AI models.
- Database persists room state to handle reconnections.
- Minimal authentication: anyone can join a room.

## Improvements (Future Scope):

- Real diff-based code merging
- Multiple language support
- Persistent session management
- Full AI-powered autocomplete
- Frontend integration with React + Redux
- Authentication for users


