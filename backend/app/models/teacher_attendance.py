from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base

class TeacherAttendance(Base):
    __tablename__ = "teacher_attendance"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    date = Column(Date, nullable=False)
    login_time = Column(DateTime, nullable=True)
    logout_time = Column(DateTime, nullable=True)
    total_hours = Column(String(50), nullable=True)  
    remarks = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    teacher = relationship("Teacher", back_populates="attendance_records")
