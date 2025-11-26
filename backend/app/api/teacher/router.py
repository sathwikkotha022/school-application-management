from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.teacher import TeacherCreate, TeacherOut, TeacherCreateFromUserId
from app.crud.teacher import create_teacher
from app.crud.user import create_user
from app.core.hashing import Hasher

router = APIRouter()


@router.post("/", response_model=TeacherOut)
def create_teacher_with_user(payload: TeacherCreate, db: Session = Depends(get_db)):

    # 1. Create User
    password_hash = Hasher.get_password_hash(payload.user.password)

    user = create_user(
        db=db,
        username=payload.user.username,
        email=payload.user.email,
        password_hash=password_hash,
        first_name=payload.user.first_name,
        last_name=payload.user.last_name,
        role="teacher"
    )

    # 2. Create Teacher
    teacher = create_teacher(
        db=db,
        user_id=user.id,
        employee_id=payload.employee_id,
        qualification=payload.qualification,
        phone=payload.phone
    )

    return teacher
