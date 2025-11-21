# app/api/admin/academic.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models
from app.schemas import marks as marks_schemas
from app.schemas import user as user_schemas
from app.core.security import get_current_active_user

router = APIRouter(prefix="/admin/academic", tags=["admin-academic"])

def ensure_admin(user: models.User):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")

@router.post("/classes")
def create_class(name: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    obj = models.SchoolClass(name=name)
    db.add(obj); db.commit(); db.refresh(obj)
    return {"id": obj.id, "name": obj.name}

@router.post("/sections")
def create_section(class_id: int, name: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    obj = models.Section(class_id=class_id, name=name)
    db.add(obj); db.commit(); db.refresh(obj)
    return {"id": obj.id, "class_id": class_id, "name": name}

@router.post("/subjects")
def create_subject(name: str, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    obj = models.Subject(name=name)
    db.add(obj); db.commit(); db.refresh(obj)
    return {"id": obj.id, "name": obj.name}

@router.post("/assign-teacher")
def assign_teacher(teacher_id: int, subject_id: int, class_id: int, section_id: int = None, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    ensure_admin(current_user)
    obj = models.TeacherSubject(teacher_id=teacher_id, subject_id=subject_id, class_id=class_id, section_id=section_id)
    db.add(obj); db.commit(); db.refresh(obj)
    return {"id": obj.id}
