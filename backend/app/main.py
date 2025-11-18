from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text   # <-- ADD THIS

from app.api.auth.router import router as auth_router
from app.database import Base, engine, get_db   # <-- FIXED import
from app.models import user, teacher, student   # <-- Models imported once

# Create tables at startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management Backend")

# Include routers
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Backend running"}


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "connected"}
    except Exception as e:
        return {"status": "error", "details": str(e)}
