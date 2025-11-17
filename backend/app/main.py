from fastapi import FastAPI
from app.database import Base, engine
from app.api.router import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management Backend")

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Backend running"}
