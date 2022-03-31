"""Creating app

creating app object
adding configuration for app

creating login manager object
adding login route and message that user need to authorize

importing routes from views.py and models from database.py
importing custom filters for jinja
"""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Вы не авторизованы"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import jinja_filters
from app import database, views
