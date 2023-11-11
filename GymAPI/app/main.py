from fastapi import FastAPI, Depends
from app.auth.base_config import auth_backend, fastapi_users
from app.auth.schemas import UserRead, UserCreate, UserUpdate
from app.subscription.router import router as subscription_router


app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    subscription_router
)