# app/api/auth/router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.crud import user as crud_user, student as crud_student, teacher as crud_teacher
from app.core import security

router = APIRouter()

class RegisterIn(BaseModel):
    username: str
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    role: str | None = "student"
    roll_number: str | None = None
    class_id: int | None = None
    section_id: int | None = None

class LoginIn(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(payload: RegisterIn, db: Session = Depends(get_db)):
    if crud_user.get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = security.hash_password(payload.password)
    user = crud_user.create_user(db, username=payload.username, email=payload.email, password_hash=hashed,
                                 first_name=payload.first_name, last_name=payload.last_name, role=payload.role)

    response = {"message": "registered", "user_id": user.id}

    if payload.role == "student":
        if not payload.roll_number or not payload.class_id or not payload.section_id:
            raise HTTPException(status_code=400, detail="roll_number, class_id, and section_id are required for students")
        student = crud_student.create_student(db, user_id=user.id, roll_number=payload.roll_number, class_id=payload.class_id, section_id=payload.section_id)
        response["student_id"] = student.id
    elif payload.role == "teacher":
        teacher = crud_teacher.create_teacher(db, user_id=user.id)
        response["teacher_id"] = teacher.id

    return response

@router.post("/login")
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_email(db, payload.email)
    if not user or not security.verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = security.create_access_token({"user_id": user.id, "role": user.role})
    return {"message": "Login successful", "access_token": token, "user": {"id": user.id, "email": user.email, "role": user.role}}
