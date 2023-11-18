from app.auth.base_config import current_user
from app.database import get_async_session
from app.auth.models import user
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends
from app.auth.utils import get_user_db


async def get_user_by_referral_code(referral_code: str, session):
    query = select(user).where(user.c.referral_code == referral_code)
    result = await session.execute(query)
    return {'message': 'success'} if result else None
