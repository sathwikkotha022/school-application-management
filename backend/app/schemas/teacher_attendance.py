from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class TeacherAttendanceBase(BaseModel):
    teacher_id: int
    date: date


class TeacherAttendanceLogin(TeacherAttendanceBase):
    login_time: Optional[datetime] = None


class TeacherAttendanceLogout(BaseModel):
    logout_time: Optional[datetime] = None


class TeacherAttendanceOut(BaseModel):
    id: int
    teacher_id: int
    date: date
    login_time: Optional[datetime] = None
    logout_time: Optional[datetime] = None
    total_hours: Optional[str] = None

    class Config:
        orm_mode = True
