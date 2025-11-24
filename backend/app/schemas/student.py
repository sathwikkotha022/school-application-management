from pydantic import BaseModel, EmailStr
from typing import Optional


class StudentUserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


class StudentCreate(BaseModel):
    roll_number: str
    class_id: int
    section_id: int
    user: StudentUserCreate


class StudentOut(BaseModel):
    id: int
    user_id: int
    roll_number: str
    class_id: int
    section_id: int

    class Config:
        from_attributes = True
