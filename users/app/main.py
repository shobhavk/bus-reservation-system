from fastapi import FastAPI,APIRouter, Depends, status, HTTPException
from app.api import user_routes
# from app.api.bus_routes import routes
from app.api.database import engine
from app.api import model
# from sqlalchemy.orm import Session

model.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(user_routes.routes)
