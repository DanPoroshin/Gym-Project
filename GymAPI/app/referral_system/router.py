from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.auth.models import User, user
from app.referral_system.utils import get_user_by_referral_code
from app.referral_system.models import referral, Referral
from app.auth.base_config import current_user

router = APIRouter(
    prefix="/referral",
    tags=["referral"],
    responses={404: {"description": "Not found"}},
)


@router.post("/claim_referral", response_model=None)
async def add_referral_operation(referral_code: str, session: AsyncSession = Depends(get_async_session), curr_user: User = Depends(current_user)):
    referral_owner_id = await get_user_by_referral_code(referral_code, session)
    curr_user_id = curr_user.id
    curr_user_sub = curr_user.is_subscribed

    query = select(referral).where(referral.c.referral_claimer_id == curr_user_id)
    result = await session.execute(query)

    if result.all():
        raise HTTPException(status_code=400, detail="You have already claimed a referral code.")
    
    if referral_owner_id is None:
        raise HTTPException(status_code=400, detail="Invalid referral code.")
    
    if curr_user_id == referral_owner_id:
        raise HTTPException(status_code=400, detail="You cannot claim your own referral code.")

    referral_stmt = Referral(
        referral_claimer_id=curr_user_id,
        referral_owner_id=referral_owner_id,
        referral_code=referral_code,
        used = curr_user_sub,
    )

    user_stmt = user.update().where(user.c.id == referral_owner_id).values(
        referral_code_used_count=user.c.referral_code_used_count + 1
    )
    await session.execute(user_stmt)
    session.add(referral_stmt)
    await session.commit()
    return {
        "status_code": "200",
        "details": "Referral claimed successfully.",
        }

@router.get('/referral_info')
async def get_referral_info(session: AsyncSession = Depends(get_async_session), curr_user: User = Depends(current_user)):
    query = select(func.count()).where(referral.c.referral_owner_id == curr_user.id and referral.c.used == True)
    result = await session.execute(query)
    return result.scalar()

@router.get('/test')
async def test(curr_user: User = Depends(current_user)):
    return curr_user