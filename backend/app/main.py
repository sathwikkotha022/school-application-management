from fastapi import FastAPI
from app.api.auth.router import router as auth_router

app = FastAPI(title="School Management Backend")

# include routers
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Backend running"}
