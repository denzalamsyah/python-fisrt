# ========= KONEKSI DI SQLITE =========
import os
from sqlalchemy import create_engine # Fungsi ini digunakan untuk membuat koneksi ke database yang ditentukan dalam URL database.
from sqlalchemy.ext.declarative import declarative_base #Ini adalah base class untuk membuat model ORM (Object-Relational Mapping). Semua model database akan mewarisi dari Base.
from sqlalchemy.orm import sessionmaker # Fungsi ini membuat kelas sesi yang digunakan untuk berinteraksi dengan database. Sesi digunakan untuk mengeksekusi perintah ke database dan menjaga koneksi tetap terbuka.
from dotenv import load_dotenv 

load_dotenv()

# Ambil nilai ENVIRONMENT
environment = os.getenv("ENVIRONMENT")

# Tentukan URL koneksi berdasarkan environment
if environment == "production":
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
else:  # Jika tidak, asumsi adalah development
    SQLALCHEMY_DATABASE_URL = os.getenv("SQLITE_DATABASE_URL")

# Inisialisasi koneksi database
if environment == "production":
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    # Khusus untuk SQLite, perlu `connect_args={"check_same_thread": False}`
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

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


def get_db():
    db = SessionLocal()  # Membuka sesi baru (koneksi ke database)
    try:
        yield db  # Mengembalikan sesi yang terbuka ke pemanggil fungsi
    finally:
        db.close()  # Menutup sesi setelah selesai
