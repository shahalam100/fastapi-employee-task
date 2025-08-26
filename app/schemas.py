from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Auth
class Token(BaseModel):
    access_token: str   # also fixed name to snake_case
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: Optional[str] = None

# Users
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    class Config:
        from_attributes = True

# Tasks
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None

class TaskRead(TaskBase):
    id: int
    owner_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class UserWithTasks(UserRead):
    tasks: List[TaskRead] = []
