from pydantic import BaseModel, EmailStr
from typing import Optional


class TeacherUserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]


class TeacherCreate(BaseModel):
    employee_id: str
    qualification: Optional[str]
    phone: Optional[str]
    user: TeacherUserCreate


class TeacherUpdate(BaseModel):
    employee_id: Optional[str] = None
    qualification: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None


class TeacherOut(BaseModel):
    id: int
    user_id: int
    employee_id: str

    class Config:
        from_attributes = True
