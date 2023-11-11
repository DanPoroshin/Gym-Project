from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    full_name: str
    is_subscribed: bool
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    full_name: str
    email: str
    password: str
    is_subscribed: Optional[bool] = False
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    full_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_subscribed: Optional[bool]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
