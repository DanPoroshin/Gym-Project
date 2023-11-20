from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    name: str
    surname: str
    is_subscribed: bool

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    email: str
    password: str
    

class UserUpdate(schemas.BaseUserUpdate):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    password: Optional[str]
