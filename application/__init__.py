"""Creating application

creating application object
adding configuration for application

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
from .config import Config, is_role, IndexView


application = Flask(__name__)  # creating main object for application
application.config.from_object(Config)  # adding configuration
application.context_processor(lambda: dict(base="base/base.html"))  # adding variable <base> for jinja

login_manager = LoginManager(application)  # creating account object
login_manager.login_view = "login"  # adding route to redirecting unauthorized
login_manager.login_message = "Вы не авторизованы"  # and massage

db = SQLAlchemy(application)  # creating database model object

migrate = Migrate(application, db)

# creating object for admin panel
admin = Admin(
    application,
    name="School_№1060",
    template_mode='bootstrap4',
    index_view=IndexView()
)


from application import admin_panel, jinja_filters
from application import database, views
