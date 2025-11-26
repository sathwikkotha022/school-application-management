# app/api/admin/academic.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models
from app.schemas import marks as marks_schemas
from app.schemas import user as user_schemas
from app.schemas import exam as exam_schemas
from app.schemas import school_class as school_class_schemas
from app.schemas import section as section_schemas
from app.schemas import subject as subject_schemas
from app.schemas import teacher_subject as teacher_subject_schemas
from app.schemas.admin_user import RegisterAdminIn
from app.core.security import get_current_active_user, hash_password
from app.crud import user as crud_user
from app.crud import school_class as crud_school_class
from app.crud import section as crud_section

router = APIRouter(prefix="/admin/academic", tags=["admin-academic"])

def ensure_admin(user: models.User):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")

@router.post("/classes")
def create_class(payload: school_class_schemas.SchoolClassCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    obj = crud_school_class.create_class(db, name=payload.name)
    return {"id": obj.id, "name": obj.name}

@router.post("/sections")
def create_section(payload: section_schemas.SectionCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    obj = crud_section.create_section(db, name=payload.name, class_id=payload.class_id)
    return {"id": obj.id, "class_id": obj.class_id, "name": obj.name}

@router.post("/subjects")
def create_subject(payload: subject_schemas.SubjectCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    # uniqueness check
    existing_subject = db.query(models.Subject).filter(models.Subject.name == payload.name).first()
    if existing_subject:
        raise HTTPException(status_code=400, detail="Subject already exists")
    obj = models.Subject(name=payload.name)
    db.add(obj); db.commit(); db.refresh(obj)
    return {"id": obj.id, "name": obj.name}

@router.post("/assign-teacher")
def assign_teacher(payload: teacher_subject_schemas.TeacherSubjectCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    try:
        obj = models.TeacherSubject(teacher_id=payload.teacher_id, subject_id=payload.subject_id, class_id=payload.class_id, section_id=payload.section_id)
        db.add(obj); db.commit(); db.refresh(obj)
        return {"id": obj.id}
    except Exception as e:
        db.rollback()
        if "foreign key constraint" in str(e).lower():
            raise HTTPException(status_code=400, detail="Invalid teacher_id, subject_id, class_id, or section_id provided")
        raise HTTPException(status_code=500, detail="Failed to assign teacher")

@router.post("/exams")
def create_exam(payload: exam_schemas.ExamCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    from app.crud import exam as crud_exam
    obj = crud_exam.create_exam(db, name=payload.name, date=payload.date)
    return {"id": obj.id, "name": obj.name, "date": obj.date}

@router.post("/create-admin")
def create_admin(payload: RegisterAdminIn, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    # uniqueness checks
    if crud_user.get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    if crud_user.get_user_by_username(db, payload.username):
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed = hash_password(payload.password)

    try:
        db.rollback()  # clear any lingering transaction state
        with db.begin():
            user = crud_user.create_user(db,
                                         username=payload.username,
                                         email=payload.email,
                                         password_hash=hashed,
                                         first_name=payload.first_name,
                                         last_name=payload.last_name,
                                         role="admin",
                                         commit=False)
        return {"message": "admin created", "user_id": user.id}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Registration failed: {e}")
