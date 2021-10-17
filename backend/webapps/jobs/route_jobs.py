import re
from fastapi import APIRouter
from fastapi import requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.routing import Router

templates = Jinja2Templates(directory="jobboard/backend/templates")
router = APIRouter(include_in_schema=False)

@router.get("/")
def home(request:Request):
    dir(request)
    return templates.TemplateResponse("jobs/homepage.html", {"request":request})