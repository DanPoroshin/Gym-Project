from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from sqlalchemy import update, select
from app.auth.models import user as user_table
from app.auth.models import User
from app.auth.base_config import current_user


router = APIRouter(
    prefix="/subscription",
    tags=["subscription"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_subscription")
async def get_subscription(id: int, session: AsyncSession = Depends(get_async_session)):
    statement = update(user_table).where(
        user_table.c.id == id).values(is_subscribed=True)
    await session.execute(statement)
    await session.commit()

    return {"message": "success"}


@router.get("/referral")
async def get_referral(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    id = user.id
    query = select(user_table.c.referral).where(user_table.c.id == id)
    result = await session.execute(query)
    result = result.scalar()
    return result
