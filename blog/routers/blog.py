from typing import List
from fastapi import APIRouter, Depends, status
from .. import schema, database
from sqlalchemy.orm import Session
from .. repository import blog
from  .oauth2 import get_current_user

router = APIRouter(
    prefix='/blog', # membuat rute diawali dengan /blog kalau digolang kaya grup
    tags=['Blogs'] # menambah tag blogs secara efektif
)

'''Blog Endpoint'''
# get blog
@router.get('/', response_model=List[schema.ShowBlog]) #menampilkan tanpa id
def all(db:Session = Depends(database.get_db), current_user: schema.User = Depends(get_current_user)):
   return blog.get_all(db)

# add blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog, db:Session = Depends(database.get_db), current_user: schema.User = Depends(get_current_user)):
  return blog.create(request,db)

# get by id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowBlog) # response_model=schema.ShowBlog --> supaya response tidak menampilkan id (sesuai dengan schema.showblog)
def show(id, db:Session = Depends(database.get_db), current_user: schema.User = Depends(get_current_user)):
   return blog.getBy_id(id, db)

# delete
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(id, db:Session = Depends(database.get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.delete(id, db)
     
# update
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Blog, db: Session = Depends(database.get_db), current_user: schema.User = Depends(get_current_user)):
  return blog.update(id,request, db)
