from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
db = SQLAlchemy(app)


from . import database
from . import views
