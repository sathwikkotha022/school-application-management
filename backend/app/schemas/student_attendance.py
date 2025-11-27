from pydantic import BaseModel, Field
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
        from_attributes : True

class StudentAttendanceAssign(BaseModel):
    teacher_id: int
    subject_id: int
    class_id: int
    section_id: int
    attendance_date: date = Field(default_factory=date.today)
    period: int = Field(default=1)
    status: str = Field(default="PRESENT")  # Default to PRESENT
    remarks: Optional[str] = None
