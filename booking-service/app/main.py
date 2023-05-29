from fastapi import FastAPI,APIRouter, Depends, status, HTTPException
from app.api import booking_routes
from app.api import authentication
# from app.api.bus_routes import routes
from app.api.database import engine
from app.api import models
# from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(booking_routes.routes)
