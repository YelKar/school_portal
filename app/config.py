import os
from flask import request
from time import strftime


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "any_key"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def my_resp(text: str = ""):
    return f'{request.remote_addr} - - {strftime("[%d/%b/%Y %H:%M:%S]")} {text}'