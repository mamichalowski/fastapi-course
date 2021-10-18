from os import name
from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router
from webapps.base import api_router as webapp_router
from fastapi.staticfiles import StaticFiles
import uvicorn


def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)

def configure_static(app):
    app.mount("/jobboard/backend/static",StaticFiles(directory="jobboard/backend/static"),name="static")



def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    configure_static(app)
    return app







app = start_application()

#@app.get("/")
#def hello_app():
#    return {"detail":"Hello World !"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)