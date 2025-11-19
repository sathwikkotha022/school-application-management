# app/schemas/teacher_attendance.py
from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional

class TeacherAttendanceBase(BaseModel):
    teacher_id: int
    date: date

class TeacherAttendanceCreate(BaseModel):
    teacher_id: int
    date: date
    login_time: Optional[datetime] = None
    logout_time: Optional[datetime] = None
    remarks: Optional[str] = None

class TeacherAttendanceOut(TeacherAttendanceBase):
    id: int
    login_time: Optional[datetime]
    logout_time: Optional[datetime]
    total_hours: Optional[str]
    created_at: Optional[datetime]

    model_config = {"from_attributes": True}

