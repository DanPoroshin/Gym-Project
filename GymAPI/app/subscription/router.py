from fastapi import APIRouter, Depends
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.base_config import current_user
from app.auth.models import User
from app.database import get_async_session
from app.referral_system.models import referral

router = APIRouter(
    tags=["subscription"],
    responses={404: {"description": "Not found"}},
)


@router.post('/subscribe', status_code=200)
async def subscribe(curr_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    curr_user.is_subscribed = True
    session.add(curr_user)
    stmt = update(referral).where(
        referral.c.referral_claimer_id == curr_user.id).values(used=True)
    await session.execute(stmt)
    await session.commit()

    return {
        "status_code": "200",
        "details": "You are now subscribed."
    }


@router.post('/unsubscribe', status_code=200)
async def unsubscribe(curr_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    curr_user.is_subscribed = False
    session.add(curr_user)
    stmt = update(referral).where(
        referral.c.referral_claimer_id == curr_user.id).values(used=False)
    await session.execute(stmt)
    await session.commit()

    return {
        "status_code": "200",
        "details": "You are now unsubscribed."
    }


@router.get('/status')
async def status(curr_user: User = Depends(current_user)):
    return {
        "is_subscribed": curr_user.is_subscribed
    }
