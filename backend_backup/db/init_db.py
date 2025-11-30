# backend/db/init_db.py
from backend.db.database import Base, engine

# import models so they are registered with Base metadata
from backend.models.room import Room

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created.")

