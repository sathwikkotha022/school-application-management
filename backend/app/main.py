from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text  
import app.models

from app.api.auth.router import router as auth_router
from app.database import Base, engine, get_db 
from app.api.router import router as api_router
Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management Backend")

# Include routers
app.include_router(api_router, prefix="/api")


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
