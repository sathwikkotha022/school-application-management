# app/schemas/teacher.py
from pydantic import BaseModel
from typing import Optional

class TeacherBase(BaseModel):
    user_id: int

    class Config:
        from_attributes = True

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(TeacherBase):
    pass

class TeacherOut(TeacherBase):
    id: int
