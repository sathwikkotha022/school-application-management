from sqlalchemy.orm import Session
from app.models.student import Student


def create_student(db: Session, user_id: int, roll_number: str,
                   class_id: int, section_id: int, commit=True):
    student = Student(
        user_id=user_id,
        roll_number=roll_number,
        class_id=class_id,
        section_id=section_id
    )
    db.add(student)
    if commit:
        db.commit()
        db.refresh(student)
    return student


def get_student_by_user_id(db: Session, user_id: int):
    return db.query(Student).filter(Student.user_id == user_id).first()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_students_by_class_section(db: Session, class_id: int, section_id: int):
    return db.query(Student).filter(Student.class_id == class_id, Student.section_id == section_id).all()
