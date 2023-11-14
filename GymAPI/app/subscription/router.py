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


@router.post('/subscribe', status_code=200)
async def subscribe(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    user.is_subscribed = True
    session.add(user)
    await session.commit()
    return 'success'

@router.post('/unsubscribe', status_code=200)
async def unsubscribe(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    user.is_subscribed = False
    session.add(user)
    await session.commit()
    return 'success'