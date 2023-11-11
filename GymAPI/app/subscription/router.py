from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from sqlalchemy import update
from app.auth.models import user

router = APIRouter(
    prefix="/subscription",
    tags=["subscription"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_subscription")
async def get_subscription(id: int, session: AsyncSession = Depends(get_async_session)):
    statement = update(user).where(user.c.id == id).values(is_subscribed=True)
    await session.execute(statement)
    await session.commit()

    return {"message": "success"}
