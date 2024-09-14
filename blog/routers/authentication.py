# ===== AUTENTIKASI =====
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schema, database, models
from sqlalchemy.orm import Session
from .. hashing import Hash
from . import jwt_token
from datetime import timedelta
from . import jwt_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Authentication']
    )

@router.post('/login')
# request: OAuth2PasswordRequestForm = Depends(): Ini menggunakan OAuth2PasswordRequestForm, 
# yang merupakan skema standar untuk otentikasi OAuth2 berbasis password. 
# Parameter ini mengharuskan pengguna mengirimkan username (email) dan password dalam request body.
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credential")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    # generate jwt token and return
    access_token = jwt_token.create_access_token(
        data={"sub": user.email} # data={"sub": user.email}: Informasi yang dimasukkan ke dalam token adalah email pengguna (sub biasanya digunakan untuk subjek, dalam hal ini adalah pengguna).
    )
    return {"access_token": access_token, "token_type": "bearer"}
