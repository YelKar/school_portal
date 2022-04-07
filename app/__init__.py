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
from flask_admin import Admin
from .config import Config


app = Flask(__name__)  # creating main object for app
app.config.from_object(Config)  # adding configuration
app.context_processor(lambda: dict(base="base/base.html"))  # adding variable <base> for jinja

login_manager = LoginManager(app)  # creating account object
login_manager.login_view = "login"  # adding route to redirecting unauthorized
login_manager.login_message = "Вы не авторизованы"  # and massage

db = SQLAlchemy(app)  # creating database model object

migrate = Migrate(app, db)

admin = Admin(app, name="School_№1060", template_mode='bootstrap4')  # creating object for admin panel


from app import admin_panel

from app import jinja_filters
from app import database, views
