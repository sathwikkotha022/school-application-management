from sqlalchemy import Column, Integer, ForeignKey, Float, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base


class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)

    marks_obtained = Column(Float, nullable=True)
    grade = Column(String(10), nullable=True)
    remarks = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    student = relationship("Student")
    teacher = relationship("Teacher")
    subject = relationship("Subject")
    school_class = relationship("SchoolClass")
    section = relationship("Section")
    exam = relationship("Exam")
