from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TeacherSubjectBase(BaseModel):
    teacher_id: int
    subject_id: int
    class_id: Optional[int] = None
    section_id: Optional[int] = None

class TeacherSubjectCreate(TeacherSubjectBase):
    pass

class TeacherSubjectOut(TeacherSubjectBase):
    id: int
    created_at: Optional[datetime]

    model_config = {"from_attributes": True}
