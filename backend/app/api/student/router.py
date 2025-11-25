from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.student import StudentCreate, StudentOut
from app.crud.student import create_student, get_student_by_user_id
from app.crud.user import create_user, get_user_by_email, get_user_by_username
from app.core.hashing import Hasher  # If you use hashing
from app.core.security import get_current_student

router = APIRouter()


@router.post("/", response_model=StudentOut)
def create_student_with_user(payload: StudentCreate, db: Session = Depends(get_db)):
    # uniqueness checks
    if get_user_by_email(db, payload.user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if get_user_by_username(db, payload.user.username):
        raise HTTPException(status_code=400, detail="Username already taken")

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


@router.get("/me", response_model=StudentOut)
def get_my_profile(current_user=Depends(get_current_student), db: Session = Depends(get_db)):
    student = get_student_by_user_id(db, current_user.id)
    if not student:
        raise HTTPException(status_code=404, detail="Student profile not found")
    return student
