from sqlalchemy import select, and_
from sqlalchemy.sql import func

from app.auth.models import user
from app.referral_system.models import referral


async def get_user_by_referral_code(referral_code: str, session) -> int:
    query = select(user).where(user.c.referral_code == referral_code)
    result = await session.execute(query)

    return result.scalar()


async def referral_info(session, curr_user) -> dict:
    query = select(referral).where(
        and_(referral.c.referral_owner_id ==
             curr_user.id, referral.c.used == True)
    )
    result = await session.execute(query)
    active_referrals = result.scalar()

    response = {
        "referral_code": curr_user.referral_code,
        "referral_code_used_count": curr_user.referral_code_used_count,
        "active_referrals": active_referrals if active_referrals else 0,
    }

    return response
