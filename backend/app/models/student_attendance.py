# app/models/student_attendance.py
from sqlalchemy import Column, Integer, Date, String, ForeignKey, TIMESTAMP, text, Enum
from sqlalchemy.orm import relationship
from app.database import Base

attendance_status_enum = Enum("present", "absent", name="attendance_status")

class StudentAttendance(Base):
    __tablename__ = "student_attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False, index=True)
    period = Column(Integer, nullable=False)  # period number e.g., 1,2,3...
    status = Column(attendance_status_enum, nullable=False, default="present")
    subject = Column(String(100), nullable=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"), nullable=True)
    remarks = Column(String(500), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"), nullable=False)

    student = relationship("Student", back_populates="attendance_records")
    teacher = relationship("Teacher", back_populates="student_attendance_records")
