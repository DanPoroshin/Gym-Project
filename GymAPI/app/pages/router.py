from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.auth.base_config import optional_current_user


router = APIRouter(
    tags=["Pages"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/home", response_class=HTMLResponse)
def get_base_page(request: Request, curr_user=Depends(optional_current_user)):
    return templates.TemplateResponse("home.html", {"request": request, "curr_user": curr_user})

