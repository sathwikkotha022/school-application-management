from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base

class TeacherSubject(Base):
    __tablename__ = "teacher_subjects"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=True)  # optional
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)  # optional
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    teacher = relationship("Teacher")
    subject = relationship("Subject")
    school_class = relationship("SchoolClass")
    section = relationship("Section")
