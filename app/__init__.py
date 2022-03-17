from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)


from app import database, views
