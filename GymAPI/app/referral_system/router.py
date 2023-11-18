from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_async_session
from app.referral_system.utils import get_user_by_referral_code


router = APIRouter(
    prefix="/referral",
    tags=["referral"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_user_by_referral")
async def get_user_by_referral(referral_code: str, session: AsyncSession = Depends(get_async_session)):
    user_id = await get_user_by_referral_code(referral_code, session)
    return user_id
