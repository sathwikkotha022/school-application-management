# app/api/auth/router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

from app.database import get_db
from app.crud import user as crud_user, student as crud_student, teacher as crud_teacher
from app.core import security

router = APIRouter(tags=["Auth"])


class RegisterStudentIn(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    roll_number: str
    class_id: int
    section_id: int


class RegisterTeacherIn(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    employee_id: Optional[str] = None
    qualification: Optional[str] = None
    phone: Optional[str] = None


class LoginIn(BaseModel):
    email: EmailStr
    password: str


@router.post("/register-student", status_code=201)
def register_student(payload: RegisterStudentIn, db: Session = Depends(get_db)):
    # uniqueness checks
    if crud_user.get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud_user.get_user_by_username(db, payload.username):
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed = security.hash_password(payload.password)

    # atomic transaction: create user + student
    try:
        db.rollback()  # clear any lingering transaction state
        with db.begin():  # will commit at exit or rollback on exception
            user = crud_user.create_user(db,
                                         username=payload.username,
                                         email=payload.email,
                                         password_hash=hashed,
                                         first_name=payload.first_name,
                                         last_name=payload.last_name,
                                         role="student",
                                         commit=False)
            db.flush()  # flush to get user.id
            student = crud_student.create_student(db,
                                                  user_id=user.id,
                                                  roll_number=payload.roll_number,
                                                  class_id=payload.class_id,
                                                  section_id=payload.section_id,
                                                  commit=False)
        return {"message": "student registered", "user_id": user.id, "student_id": student.id}
    except HTTPException:
        raise
    except Exception as e:
        # log if you have logging; return generic error
        raise HTTPException(status_code=500, detail=f"Registration failed: {e}")


@router.post("/register-teacher", status_code=201)
def register_teacher(payload: RegisterTeacherIn, db: Session = Depends(get_db)):
    if crud_user.get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud_user.get_user_by_username(db, payload.username):
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed = security.hash_password(payload.password)

    try:
        db.rollback()  # clear any lingering transaction state
        with db.begin():
            user = crud_user.create_user(db,
                                         username=payload.username,
                                         email=payload.email,
                                         password_hash=hashed,
                                         first_name=payload.first_name,
                                         last_name=payload.last_name,
                                         role="teacher",
                                         commit=False)
            teacher = crud_teacher.create_teacher(db,
                                                  user_id=user.id,
                                                  employee_id=payload.employee_id,
                                                  qualification=payload.qualification,
                                                  phone=payload.phone,
                                                  commit=False)
        return {"message": "teacher registered", "user_id": user.id, "teacher_id": teacher.id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Registration failed: {e}")


@router.post("/login")
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_email(db, payload.email)
    if not user or not security.verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = security.create_access_token({"user_id": user.id, "role": user.role})
    return {"message": "Login successful", "access_token": token, "token_type": "bearer", "user": {"id": user.id, "email": user.email, "role": user.role}}
