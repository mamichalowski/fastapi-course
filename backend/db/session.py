from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE)

SessionLocal = sessionmaker(autocommit = False,autoflush = False, bind=engine)