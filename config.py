import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-neber-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False