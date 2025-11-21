from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    role: str
    is_active: bool

    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    user: UserResponse

