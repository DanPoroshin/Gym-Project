from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth.models import User, user
from app.auth.base_config import current_user
from app.database import get_async_session
router = APIRouter(
    prefix="/referral",
    tags=["referral"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_user_by_referral")
async def get_user_by_referral(referral_code: str, session: AsyncSession = Depends(get_async_session)):
    query = select(user).where(user.c.referral_code == referral_code)
    result = await session.execute(query)
    return result.scalar()

