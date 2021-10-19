from fastapi import APIRouter
from fastapi import templating
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates("jobboard/backend/templates")
router = APIRouter(include_in_schema=False)

@router.get("/login/")
def login(request:Request):
    return templates.TemplateResponse("auth/login.html",{"request":request})