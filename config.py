import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Base SQLite stockée dans ton projet sous le nom app.db
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "change-moi-en-valeur-secrète"
