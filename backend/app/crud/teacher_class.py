# app/crud/teacher_class.py
from sqlalchemy.orm import Session
from typing import List, Dict, Optional

from app import models

def get_teacher_classes(db: Session, teacher_id: int) -> List[Dict]:
    """
    Try multiple strategies:
    1) If a mapping model `TeacherClass` or `TeacherAssignment` exists, use it.
    2) Fall back to scanning Teacher relationships if present.
    Returns a list of dicts {class_id, class_name, section_id, section_name, subject_id, subject_name}
    """
    results = []

    # Strategy 1: explicit mapping table model present
    try:
        # expecting a model named TeacherClass or TeacherAssignment
        if hasattr(models, "TeacherClass"):
            mapping_q = db.query(models.TeacherClass).filter(models.TeacherClass.teacher_id == teacher_id).all()
            for m in mapping_q:
                class_name = getattr(m, "school_class", None)
                section = getattr(m, "section", None)
                subject = getattr(m, "subject", None)
                results.append({
                    "mapping_id": getattr(m, "id", None),
                    "class_id": getattr(m, "class_id", None),
                    "class_name": getattr(class_name, "name", None) if class_name else None,
                    "section_id": getattr(m, "section_id", None),
                    "section_name": getattr(section, "name", None) if section else None,
                    "subject_id": getattr(m, "subject_id", None),
                    "subject_name": getattr(subject, "name", None) if subject else None,
                })
            return results
    except Exception:
        pass

    # Strategy 2: try teacher -> attendance / marks relations to infer classes
    try:
        teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
        if teacher:
            # check marks relation
            if hasattr(teacher, "attendance_records") and teacher.attendance_records:
                for a in teacher.attendance_records:
                    c = getattr(a, "school_class", None)
                    s = getattr(a, "section", None)
                    results.append({
                        "class_id": getattr(a, "class_id", None),
                        "class_name": getattr(c, "name", None) if c else None,
                        "section_id": getattr(a, "section_id", None),
                        "section_name": getattr(s, "name", None) if s else None,
                    })
            # check student_attendance records teacher may have
            if hasattr(teacher, "student_attendance_records") and teacher.student_attendance_records:
                for sa in teacher.student_attendance_records:
                    # student-attendance has student -> student.grade? Not ideal; skip
                    pass
    except Exception:
        pass

    # dedupe results by class_id & section_id
    seen = set()
    deduped = []
    for r in results:
        key = (r.get("class_id"), r.get("section_id"), r.get("subject_id"))
        if key not in seen:
            seen.add(key)
            deduped.append(r)
    return deduped
