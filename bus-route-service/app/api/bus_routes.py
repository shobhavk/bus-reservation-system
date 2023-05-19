from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.api import database, database_manager
from app.api.model import BusRoute
from app.api import schema

routes = APIRouter(
    prefix="/busroutes",
    tags=['BusRoutes']
)


get_db = database.get_db

@routes.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schema.BusRoute, db: Session= Depends(get_db)):
   return database_manager.create(request, db)      

# @routes.get('/', response_model=List[MovieOut])
# async def get_movies():
#     return await db_manager.get_all_movies()

# @routes.get('/{id}/', response_model=MovieOut)
# async def get_movie(id: int):
#     movie = await db_manager.get_movie(id)
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return movie

# @routes.put('/{id}/', response_model=MovieOut)
# async def update_movie(id: int, payload: MovieUpdate):
#     movie = await db_manager.get_movie(id)
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")

#     update_data = payload.dict(exclude_unset=True)

#     if 'casts_id' in update_data:
#         for cast_id in payload.casts_id:
#             if not is_cast_present(cast_id):
#                 raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

#     movie_in_db = MovieIn(**movie)

#     updated_movie = movie_in_db.copy(update=update_data)

#     return await db_manager.update_movie(id, updated_movie)

# @routes.delete('/{id}/', response_model=None)
# async def delete_movie(id: int):
#     movie = await db_manager.get_movie(id)
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return await db_manager.delete_movie(id)