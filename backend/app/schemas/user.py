from pydantic import BaseModel, EmailStr
from typing import Optional

# ---------------------------------------------------------
# Base User schema (shared attributes)
# ---------------------------------------------------------
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    role: Optional[str] = None   # admin, teacher, student


# ---------------------------------------------------------
# Schema for creating a user
# ---------------------------------------------------------
class UserCreate(UserBase):
    password: str


# ---------------------------------------------------------
# Schema for updating a user
# ---------------------------------------------------------
class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None


# ---------------------------------------------------------
# Schema returned to client (THIS IS THE MISSING ONE)
# ---------------------------------------------------------
class UserOut(UserBase):
    id: int

    model_config = {"from_attributes": True}



# ---------------------------------------------------------
# Schema with password hash (internal only)
# ---------------------------------------------------------
class UserInDB(UserBase):
    id: int
    hashed_password: str

    model_config = {"from_attributes": True}

