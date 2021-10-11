from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router
import uvicorn


def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app







app = start_application()

@app.get("/")
def hello_app():
    return {"detail":"Hello World !"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)