from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schema, models, database,hashing
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


'''User Endpoint'''
# post user
@router.post('/')
def create_user(request:schema.User, db:Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

# get user
@router.get('/', response_model=List[schema.ShowUser]) #menampilkan tanpa id dan password
def all_user(db:Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users


# get by id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowUser) # response_model=schema.ShowBlog --> supaya response tidak menampilkan id (sesuai dengan schema.showblog)
def show_user(id, response:Response, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        '''menggunakan Http exception dari fastAPI'''
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user

# delete
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id, db:Session = Depends(database.get_db)):
     user = db.query(models.User).filter(models.User.id == id).first()
     if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
     else:
        db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail='User is deleted')
     