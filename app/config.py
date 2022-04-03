import os
from flask import request
from time import strftime


class Config(object):
    """
    adding configuration to app
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or "any_key"  # Creating secret key for forms
    DEBUG = True  # Activating debug mode
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.db"  # route to database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "solar"


def my_resp(text: str = ""):
    return f'{request.remote_addr} - - {strftime("[%d/%b/%Y %H:%M:%S]")} {text}'
