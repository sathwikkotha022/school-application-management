# app/crud/teacher.py
from sqlalchemy.orm import Session
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate

def create_teacher(db: Session, user_id: int,
                   employee_id: str = None,
                   qualification: str = None,
                   phone: str = None,
                   commit=True):
    t = Teacher(
        user_id=user_id,
        employee_id=employee_id,
        qualification=qualification,
        phone=phone
    )
    db.add(t)
    if commit:
        db.commit()
        db.refresh(t)
    return t


def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

def get_teacher_by_user_id(db: Session, user_id: int):
    return db.query(Teacher).filter(Teacher.user_id == user_id).first()

def get_teacher_by_employee_id(db: Session, employee_id: str):
    return db.query(Teacher).filter(Teacher.employee_id == employee_id).first()

def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Teacher).offset(skip).limit(limit).all()

def update_teacher(db: Session, teacher_id: int, teacher_update: TeacherUpdate):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher:
        update_data = teacher_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_teacher, field, value)
        db.commit()
        db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
    return db_teacher
