from sqlalchemy.orm import Session
from .. import schema, models
from fastapi import status, HTTPException

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create( request:schema.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog) # Menambahkan objek new_blog ke sesi database (db). 
    db.commit() # Menyimpan (commit) semua perubahan yang ditandai ke dalam database.
    db.refresh(new_blog) # Mengambil ulang data terbaru dari database untuk objek new_blog
    return new_blog

def getBy_id(id, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        '''menggunakan Http exception dari fastAPI'''
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog

def delete(id, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
  
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'blog is deleted'

def update(id, request:schema.Blog, db:Session):
    # cara alternative, bisa juga seperti pada update
    blogs = models.Blog
    blog = db.query(blogs).filter(blogs.id== id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    blog.update(dict(request), synchronize_session=False)
    db.commit()
    return 'updated'