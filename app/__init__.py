from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
import datetime


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Вы не авторизованы"

db = SQLAlchemy(app)

migrate = Migrate(app, db)


@app.template_filter("fromTimestamp")
def from_timestamp_filter(product):
    return datetime.datetime.fromtimestamp(product)


@app.template_filter("strftime")
def strftime_filter(product: datetime.datetime, form: str):
    return product.strftime(form)


from app import database, views
