from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api import database
import requests

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends()):
    response =  requests.post(
        f"http://user_service:8004/user/login", request=request
    )
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
