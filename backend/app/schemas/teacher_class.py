from pydantic import BaseModel
from typing import Optional


class TeacherClassBase(BaseModel):
    teacher_id: int
    class_id: int
    section_id: int
    subject_id: Optional[int] = None


class TeacherClassCreate(TeacherClassBase):
    pass


class TeacherClassOut(BaseModel):
    mapping_id: Optional[int] = None
    class_id: Optional[int] = None
    class_name: Optional[str] = None
    section_id: Optional[int] = None
    section_name: Optional[str] = None
    subject_id: Optional[int] = None
    subject_name: Optional[str] = None

    class Config:
        orm_mode = True
