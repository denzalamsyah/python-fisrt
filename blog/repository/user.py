from sqlalchemy.orm import Session
from .. import models, hashing
from fastapi import status, HTTPException

def create(request:models.User, db:Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db:Session):
    users = db.query(models.User).all()
    return users

def getBy_id(id, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        '''menggunakan Http exception dari fastAPI'''
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user

def delete(id, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return 'User is deleted'