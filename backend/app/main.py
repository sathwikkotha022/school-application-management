from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text  
import app.models
from app.models import teacher_class

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
