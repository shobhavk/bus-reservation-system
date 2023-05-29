from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.api import database, database_manager, schemas, oauth2, token, model
from app.api.model import User
from app.api.hashing import Hash

from fastapi.security import OAuth2PasswordRequestForm


routes = APIRouter(
    prefix="/user",
    tags=['Users']
)


get_db = database.get_db


@routes.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return database_manager.create(request, db)


@routes.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return database_manager.show(id, db)


@routes.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    print("this is request from booking", request)
    user = db.query(model.User).filter(
        model.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@routes.post('/validate/{user_token}', status_code=200)
def validate_token(user_token: str):
    print("it  came heere")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(user_token, credentials_exception)