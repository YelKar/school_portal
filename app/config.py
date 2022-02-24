import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "any_key"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
