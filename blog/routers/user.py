from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schema, models, database,hashing
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


'''User Endpoint'''
# post user
@router.post('/')
def create_user(request:schema.User, db:Session = Depends(database.get_db)):
    return user.create(request, db)

# get user
@router.get('/', response_model=List[schema.ShowUser]) #menampilkan tanpa id dan password
def all_user(db:Session = Depends(database.get_db)):
    return user.get_all(db)


# get by id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowUser) # response_model=schema.ShowBlog --> supaya response tidak menampilkan id (sesuai dengan schema.showblog)
def show_user(id, db:Session = Depends(database.get_db)):
    return user.getBy_id(id, db)

# delete
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_user(id, db:Session = Depends(database.get_db)):
    return user.delete(id, db)
     