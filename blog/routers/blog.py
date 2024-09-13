from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schema, models, database
from sqlalchemy.orm import Session

router = APIRouter()

'''Blog Endpoint'''
# get blog
# @router.get('/blog', tags=['blogs'])
@router.get('/blog', response_model=List[schema.ShowBlog], tags=['blogs']) #menampilkan tanpa id
def all(db:Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# add blog
@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schema.Blog, db:Session = Depends(database.get_db)):
   new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
   db.add(new_blog) # Menambahkan objek new_blog ke sesi database (db). 
   db.commit() # Menyimpan (commit) semua perubahan yang ditandai ke dalam database.
   db.refresh(new_blog) # Mengambil ulang data terbaru dari database untuk objek new_blog
   return new_blog

# get by id
@router.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowBlog, tags=['blogs']) # response_model=schema.ShowBlog --> supaya response tidak menampilkan id (sesuai dengan schema.showblog)
def show(id, response:Response, db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        '''menggunakan Http exception dari fastAPI'''
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    
        '''menggunakan response biasa'''
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with the id {id} is not available"}
    return blog

# delete
@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete(id, db:Session = Depends(database.get_db)):
     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
     if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
     else:
        db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail='blog is deleted')
     
# update
@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id: int, request: schema.Blog, db: Session = Depends(database.get_db)):
    # cara alternative, bisa juga seperti pada update
    blogs = models.Blog
    blog = db.query(blogs).filter(blogs.id== id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    blog.update(dict(request), synchronize_session=False)
    db.commit()
    return 'updated'
