from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.auth.base_config import auth_backend, fastapi_users
from app.auth.schemas import UserCreate, UserRead, UserUpdate
from app.pages.router import router as pages_router
from app.referral_system.router import router as referral_system_router
from app.subscription.router import router as subscription_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="app\static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
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
    subscription_router,
    prefix="/subscription",
)

app.include_router(
    referral_system_router,
)

app.include_router(
    pages_router,
)
