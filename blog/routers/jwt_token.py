# ===== FUNGSI UNTUK MEMBUAT TOKEN JWT =====
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from .. import schema

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256" # Hh-based Message Authentication Code merujuk pada algoritma kriptografi yang digunakan untuk menandatangani dan memverifikasi token JWT (JSON Web Token).
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Fungsi ini digunakan untuk membuat token JWT yang berisi data pengguna serta masa kadaluarsa token.
def create_access_token(data: dict): # data: dict: Fungsi ini menerima parameter data, yang biasanya merupakan informasi pengguna (misalnya, email, user_id, atau username).
    to_encode = data.copy() #  Menyalin data input menjadi dictionary baru yang akan di-encode menjadi JWT.
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # Membuat waktu kadaluarsa token, yaitu dengan menambahkan beberapa menit (didefinisikan oleh ACCESS_TOKEN_EXPIRE_MINUTES) dari waktu saat ini. Token akan valid hanya sampai waktu ini.
    to_encode.update({"exp": expire}) # Menambahkan field "exp" ke dalam to_encode, yang merupakan waktu kadaluarsa token (expiration time).
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # Token JWT dihasilkan dengan menggunakan SECRET_KEY, ALGORITHM 
    return encoded_jwt # Mengembalikan token JWT yang sudah dienkripsi.

# Fungsi ini digunakan untuk memverifikasi token JWT yang diterima dari pengguna
# Jika token valid, data pengguna akan diekstraksi dari token tersebut.
def veriy_token(token:str, credentials_exception): # credentials_exception: Exception (kesalahan) yang akan dilemparkan jika token tidak valid.
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # Token JWT didekode dengan menggunakan SECRET_KEY yang sama dan algoritma yang sesuai.
        email: str = payload.get("sub") # Mengambil data sub (subject), yang dalam banyak kasus merupakan identitas unik pengguna (misalnya email atau user ID).
        if email is None:
            raise credentials_exception
        token_data = schema.TokenData(email=email) # ka email valid, data token (misalnya, email pengguna) akan disimpan dalam variabel token_data
    except InvalidTokenError:
        raise credentials_exception
   