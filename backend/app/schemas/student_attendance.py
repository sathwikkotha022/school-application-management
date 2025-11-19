# app/schemas/student_attendance.py
from datetime import date
from pydantic import BaseModel
from typing import Optional

class StudentAttendanceBase(BaseModel):
    student_id: int
    date: date
    period: int
    status: str
    subject: Optional[str] = None
    teacher_id: Optional[int] = None
    remarks: Optional[str] = None

class StudentAttendanceCreate(StudentAttendanceBase):
    pass

class StudentAttendanceUpdate(BaseModel):
    status: Optional[str] = None
    remarks: Optional[str] = None

class StudentAttendanceOut(StudentAttendanceBase):
    id: int
    created_at: Optional[str]

    model_config = {"from_attributes": True}

