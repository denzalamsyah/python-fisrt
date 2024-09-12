from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schema, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()  # Membuka sesi baru (koneksi ke database)
    try:
        yield db  # Mengembalikan sesi yang terbuka ke pemanggil fungsi
    finally:
        db.close()  # Menutup sesi setelah selesai

# add blog
# @app.post('/blog', status_code=201)
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog, db:Session = Depends(get_db)):
# db: Session = Depends(get_db): db adalah sesi database yang diperoleh dari 
# dependensi get_db. Depends(get_db) memastikan bahwa setiap kali fungsi ini 
# dipanggil, sesi ke database akan tersedia, dan db adalah objek sesi yang 
# bisa digunakan untuk berinteraksi dengan database (menambah, mengubah, menghapus data).
   new_blog = models.Blog(title=request.title, body=request.body)
   db.add(new_blog) # Menambahkan objek new_blog ke sesi database (db). 
   db.commit() # Menyimpan (commit) semua perubahan yang ditandai ke dalam database.
   db.refresh(new_blog) # Mengambil ulang data terbaru dari database untuk objek new_blog
   return new_blog

# get blog
@app.get('/blog')
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# get by id
@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id, response:Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        '''menggunakan Http exception dari fastAPI'''
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    
        '''menggunakan response biasa'''
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail' : f"Blog with the id {id} is not available"}
    return blog

# delete
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db:Session = Depends(get_db)):
     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
     if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
     else:
        db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail='blog is deleted')
     
# update
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Blog, db: Session = Depends(get_db)):
    # cara alternative, bisa juga seperti pada update
    blogs = models.Blog
    blog = db.query(blogs).filter(blogs.id== id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")

    blog.update(dict(request), synchronize_session=False)
    db.commit()
    return 'updated'
