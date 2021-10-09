from typing import Optional
from typing_extensions import ParamSpecKwargs
from pydantic import BaseModel,EmailStr


class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str