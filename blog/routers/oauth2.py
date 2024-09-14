from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated
from . import jwt_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # OAuth2PasswordBearer, yang digunakan untuk mengambil token dari header "Authorization" dengan format "Bearer <token>" pada endpoint login

# Ini adalah sebuah fungsi asinkron (async def) yang bertujuan untuk mendapatkan pengguna saat ini berdasarkan token yang dikirimkan.
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]): # Menggunakan Depends(oauth2_scheme) untuk mengekstrak token dari request HTTP yang diterima, yaitu dari skema OAuth2 Bearer yang didefinisikan sebelumnya.
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
   
    return jwt_token.veriy_token(token, credentials_exception)