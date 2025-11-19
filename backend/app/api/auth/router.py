from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.user import User
from app.models.teacher import Teacher
from app.models.student import Student
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(tags=["Auth"])

# =====================
# 📌 SCHEMAS
# =====================

class RegisterTeacher(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    name: str
    subject: str


class RegisterStudent(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str
    name: str
    grade: str


class Login(BaseModel):
    email: str
    password: str


# =============================
# 📌 REGISTER TEACHER
# =============================

@router.post("/register/teacher")
def register_teacher(data: RegisterTeacher, db: Session = Depends(get_db)):

    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create User entry
    user = User(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password),
        first_name=data.first_name,
        last_name=data.last_name,
        role="teacher",
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Create Teacher entry
    teacher = Teacher(
        user_id=user.id,
        name=data.name,
        subject=data.subject
    )
    db.add(teacher)
    db.commit()

    return {"message": "Teacher registered successfully", "teacher_id": teacher.id}


# =============================
# 📌 REGISTER STUDENT
# =============================

@router.post("/register/student")
def register_student(data: RegisterStudent, db: Session = Depends(get_db)):

    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create User entry
    user = User(
        username=data.username,
        email=data.email,
        password_hash=hash_password(data.password),
        first_name=data.first_name,
        last_name=data.last_name,
        role="student",
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Create Student entry
    student = Student(
        user_id=user.id,
        name=data.name,
        grade=data.grade
    )
    db.add(student)
    db.commit()

    return {"message": "Student registered successfully", "student_id": student.id}


# =============================
# 📌 LOGIN
# =============================

@router.post("/login")
def login(data: Login, db: Session = Depends(get_db)):

    # Find user
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Verify password
    if not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Create JWT token
    token = create_access_token({"user_id": user.id, "role": user.role})

    return {
        "message": "Login successful",
        "access_token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    }
