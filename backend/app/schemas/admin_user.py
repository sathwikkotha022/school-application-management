from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class AdminUserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = "student"
    class_id: Optional[int] = None
    section_id: Optional[int] = None

class RegisterAdminIn(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
