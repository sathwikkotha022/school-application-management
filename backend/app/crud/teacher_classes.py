# app/crud/teacher_classes.py
from sqlalchemy.orm import Session
from typing import List, Dict
from app import models

def get_teacher_classes(db: Session, teacher_id: int) -> List[Dict]:
    results = []

    # 1. Direct mapping table
    if hasattr(models, "TeacherClass"):
        mapping = (
            db.query(models.TeacherClass)
            .filter(models.TeacherClass.teacher_id == teacher_id)
            .all()
        )

        for m in mapping:
            results.append({
                "mapping_id": m.id,
                "class_id": m.class_id,
                "class_name": m.school_class.name if m.school_class else None,
                "section_id": m.section_id,
                "section_name": m.section.name if m.section else None,
                "subject_id": m.subject_id,
                "subject_name": m.subject.name if m.subject else None
            })

    return results
