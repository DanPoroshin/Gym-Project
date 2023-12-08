from pydantic import BaseModel


class ReferralInfo(BaseModel):
    referral_times_activated: int
    current_user_referral: str
    referral_code_used_count: int


class ReferralCode(BaseModel):
    code: str
