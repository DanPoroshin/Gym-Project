from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.base_config import optional_current_user
from app.database import get_async_session
from app.referral_system.utils import referral_info

router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def get_base_page(request: Request, curr_user=Depends(optional_current_user)):
    return templates.TemplateResponse("home.html", {"request": request, "curr_user": curr_user})


@router.get("/login", response_class=HTMLResponse)
def get_login_page(request: Request, curr_user=Depends(optional_current_user)):
    return templates.TemplateResponse("login.html", {"request": request, "curr_user": curr_user})


@router.get("/signup", response_class=HTMLResponse)
def get_signup_page(request: Request, curr_user=Depends(optional_current_user)):
    return templates.TemplateResponse("signup.html", {"request": request, "curr_user": curr_user})


@router.get('/contact', response_class=HTMLResponse)
def get_contact_page(request: Request, curr_user=Depends(optional_current_user)):
    return templates.TemplateResponse("contact.html", {"request": request, "curr_user": curr_user})


@router.get('/about', response_class=HTMLResponse)
def get_about_page(request: Request, curr_user=Depends(optional_current_user)):
    return templates.TemplateResponse("about.html", {"request": request, "curr_user": curr_user})


@router.get('/profile', response_class=HTMLResponse)
async def get_profile_page(request: Request, curr_user=Depends(optional_current_user), session: AsyncSession = Depends(get_async_session)):
    # Assuming you have functions to get user data, subscription status, and referral info
    subscription_status = curr_user.is_subscribed  # Update with your logic
    referral_information = await referral_info(session, curr_user)

    return templates.TemplateResponse(
        "profile.html",
        {"request": request,
         "curr_user": curr_user,
         "subscription_status": subscription_status,
         "referral_code": referral_information['referral_code'],
         "referral_code_used_count": referral_information['referral_code_used_count'],
         "active_referrals": referral_information['active_referrals']},
    )
