# app/api/auth/teacher_auth.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.teacher import Teacher

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/teacher/token")

def get_current_teacher(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Teacher:
    # Dummy example: replace with real token verification
    teacher = db.query(Teacher).first()
    if not teacher:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return teacher
