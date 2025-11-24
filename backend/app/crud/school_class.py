# app/crud/school_class.py
from sqlalchemy.orm import Session
from app.models.school_class import SchoolClass

def create_class(db: Session, name: str):
    c = SchoolClass(name=name)
    db.add(c)
    db.commit()
    db.refresh(c)
    return c

def get_class(db: Session, class_id: int):
    return db.query(SchoolClass).filter(SchoolClass.id == class_id).first()
