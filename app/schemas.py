from pydantic import BaseModel, EmailStr
import datetime

class PostBase(BaseModel):
    title: str 
    content: str 
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    title: str 
    content: str 
    published: bool = True

class UserCreate(BaseModel):
    email: EmailStr 
    password: str

class UserCreateResponse(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime.datetime

class GetUserResponse(UserCreateResponse):
    pass
