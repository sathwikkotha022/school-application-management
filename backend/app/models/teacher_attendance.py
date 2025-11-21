from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, Date, text
from app.database import Base
from sqlalchemy.orm import relationship
from app.database import Base


class TeacherAttendance(Base):
    __tablename__ = "teacher_attendance"

    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    date = Column(Date, nullable=False)
    login_time = Column(TIMESTAMP, nullable=True)
    logout_time = Column(TIMESTAMP, nullable=True)
    total_hours = Column(String(20), nullable=True)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    teacher = relationship("Teacher")
