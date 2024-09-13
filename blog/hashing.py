# ===== HASHING PASSWORD =====
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password:str):
        return pwd_context.hash(password)
# --> MASIH TERJADI KESALAHAN  version = _bcrypt.__about__.__version__ <---
# --> SOLUSINYA TURUNKAN VERSI BCYRPT NYA KE VERSI 4.0.1 ATAU 3.2.2<---
# --> 2ATAU GUNAKAN CARA DI BAWAH INI <---


# APABILA TIDAK MAU MENGGUNAKAN PASSLIB, GUNAKAN BCRYPT SAJA
# import bcrypt

# Hash a password using bcrypt
# def hash_password(password):
#     pwd_bytes = password.encode('utf-8')
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
#     return hashed_password

# # Check if the provided password matches the stored password (hashed)
# def verify_password(plain_password, hashed_password):
#     password_byte_enc = plain_password.encode('utf-8')
#     return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password)
