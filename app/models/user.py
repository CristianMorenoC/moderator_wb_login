from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None

    class Config:
        from_attributes = True
