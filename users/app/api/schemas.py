from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    password:str
    role:str

class ShowUser(BaseModel):
    name:str
    email:str
    role:str
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None