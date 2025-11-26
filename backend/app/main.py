from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
import app.models
from app.models import teacher_classes

from app.api.auth import router as auth_router
from app.database import Base, engine, get_db, SessionLocal
from app.api.router import router as api_router
from app.crud.user import get_user_by_email, get_user_by_username, create_user, get_admin_exists
from app.core.security import hash_password

Base.metadata.create_all(bind=engine)

# Seed admin user if not exists
db = SessionLocal()
try:
    admin_email = "admin@example.com"
    if not get_user_by_email(db, admin_email):
        hashed_password = hash_password("admin123")
        create_user(
            db,
            username="administrator",
            email=admin_email,
            password_hash=hashed_password,
            role="admin"
        )
        print("Admin user seeded successfully.")
finally:
    db.close()

app = FastAPI(title="School Management Backend")

# Include routers
app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Backend running"}
