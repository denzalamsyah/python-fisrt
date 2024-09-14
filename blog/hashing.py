# ===== HASHING PASSWORD =====
from passlib.context import CryptContext 

# CryptContext adalah objek dari library passlib yang digunakan untuk mengelola skema hashing.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# 1. schemes=["bcrypt"]: Menunjukkan bahwa skema hashing yang digunakan adalah bcrypt, salah satu algoritma hashing yang populer dan aman untuk hashing password.
# 2. deprecated="auto": Menunjukkan bahwa skema hashing lama akan ditandai sebagai deprecated secara otomatis jika ada skema yang lebih baru di masa mendatang.

class Hash():
    def bcrypt(password:str):
        return pwd_context.hash(password) # pwd_context.hash(password) akan melakukan hashing terhadap password menggunakan skema bcrypt yang sudah didefinisikan.
    
    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password) # akan membandingkan password asli yang diberikan oleh pengguna dengan password yang sudah di-hash di database
    
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
