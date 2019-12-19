# Try and move this and .env out into the root directory
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-never-guess'


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    BASE_URL = 'http://localhost:5000'

class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False