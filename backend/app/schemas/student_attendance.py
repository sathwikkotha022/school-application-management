from pydantic import BaseModel
from datetime import date
from typing import Optional


class StudentAttendanceBase(BaseModel):
    student_id: int
    date: date
    period: int
    status: str     # PRESENT / ABSENT
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

    class Config:
        orm_mode = True
