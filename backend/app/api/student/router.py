from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.student import StudentCreate, StudentOut
from app.crud.student import create_student
from app.crud.user import create_user
from app.core.hashing import Hasher  # If you use hashing

router = APIRouter()


@router.post("/", response_model=StudentOut)
def create_student_with_user(payload: StudentCreate, db: Session = Depends(get_db)):

    # 1. Create User
    password_hash = Hasher.get_password_hash(payload.user.password)

    user = create_user(
        db=db,
        username=payload.user.username,
        email=payload.user.email,
        password_hash=password_hash,
        first_name=payload.user.first_name,
        last_name=payload.user.last_name,
        role="student"
    )

    # 2. Create Student
    student = create_student(
        db=db,
        user_id=user.id,
        roll_number=payload.roll_number,
        class_id=payload.class_id,
        section_id=payload.section_id
    )

    return student
