# ========= KONEKSI DI SQLITE =========

from sqlalchemy import create_engine # Fungsi ini digunakan untuk membuat koneksi ke database yang ditentukan dalam URL database.
from sqlalchemy.ext.declarative import declarative_base #Ini adalah base class untuk membuat model ORM (Object-Relational Mapping). Semua model database akan mewarisi dari Base.
from sqlalchemy.orm import sessionmaker # Fungsi ini membuat kelas sesi yang digunakan untuk berinteraksi dengan database. Sesi digunakan untuk mengeksekusi perintah ke database dan menjaga koneksi tetap terbuka.


# Membuat URL koneksi ke database.
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Menginisialisasi koneksi database (engine) berdasarkan URL tersebut.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Membuat sesi untuk mengelola transaksi database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Menyediakan base class untuk membuat model ORM (tabel dalam database).
Base = declarative_base()

# ========= CONTOH KONEKSI DI POSTGRESQL =========

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Ganti dengan URL PostgreSQL sesuai dengan kredensial Anda
# SQLALCHEMY_DATABASE_URL = "postgresql://root:root@localhost/mydatabase"

# # Membuat engine untuk PostgreSQL
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

# # Membuat session
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base class untuk model database
# Base = declarative_base()
