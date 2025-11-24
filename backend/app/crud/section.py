# app/crud/section.py
from sqlalchemy.orm import Session
from app.models.section import Section

def create_section(db: Session, name: str, class_id: int):
    s = Section(name=name, class_id=class_id)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def get_section(db: Session, section_id: int):
    return db.query(Section).filter(Section.id == section_id).first()
