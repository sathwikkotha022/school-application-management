from sqlalchemy import Column, Integer, ForeignKey, String, Date, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base


class StudentAttendance(Base):
    __tablename__ = "student_attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    date = Column(Date, nullable=False)
    period = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)  # PRESENT / ABSENT
    subject = Column(String(50), nullable=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)
    remarks = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    student = relationship("Student")
    teacher = relationship("Teacher")
