import re
from fastapi import APIRouter
from fastapi import requests
from fastapi.params import Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm.session import Session
from starlette.templating import _TemplateResponse
from db.repository.jobs import list_jobs
from sqlalchemy.orm import Session
from db.session import get_db
from fastapi import Depends
from db.repository.jobs import retreive_job
from starlette.requests import Request
from starlette.routing import Router

templates = Jinja2Templates(directory="jobboard/backend/templates")
router = APIRouter(include_in_schema=False)

@router.get("/")
def home(request:Request,db:Session=Depends(get_db)):
    dir(request)
    jobs = list_jobs(db=db)
    return templates.TemplateResponse("jobs/homepage.html", {"request":request,"jobs":jobs})

@router.get("/detail/{id}")
def job_detail(id:int,request:Request,db:Session=Depends(get_db)):
    job = retreive_job(id=id,db=db)
    return templates.TemplateResponse("jobs/detail.html",{"request":request,"job":job})
