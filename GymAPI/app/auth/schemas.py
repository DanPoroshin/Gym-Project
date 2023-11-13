from typing import Optional
from fastapi_users import schemas
from secrets import token_urlsafe
from pydantic import Json


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    full_name: str
    is_subscribed: bool

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    full_name: str
    email: str
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    full_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_subscribed: Optional[bool]
