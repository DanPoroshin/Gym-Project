from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.auth.models import User, user
from app.referral_system.utils import get_user_by_referral_code
from app.referral_system.models import Referral
from app.auth.base_config import current_user

router = APIRouter(
    prefix="/referral",
    tags=["referral"],
    responses={404: {"description": "Not found"}},
)


@router.post("/submit_referral", response_model=None)
async def add_referral_operation(referral_code: str, session: AsyncSession = Depends(get_async_session), curr_user: User = Depends(current_user)):
    referral_user_id = await get_user_by_referral_code(referral_code, session)
    curr_user_id = curr_user.id

    if referral_user_id is None:
        return {"message": "Invalid referral code."}

    if curr_user_id == referral_user_id:
        return {"message": "You cannot refer yourself."}

    referral = Referral(
        referring_user_id=curr_user_id,
        referred_user_id=referral_user_id,
        referral_code=referral_code
    )
    session.add(referral)
    await session.commit()
    return {"message": "Referral added successfully."}
