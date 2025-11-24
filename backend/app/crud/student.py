from sqlalchemy.orm import Session
from app.models.student import Student


def create_student(db: Session, user_id: int, roll_number: str, class_id: int, section_id: int):
    student = Student(
        user_id=user_id,
        roll_number=roll_number,
        class_id=class_id,
        section_id=section_id
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
