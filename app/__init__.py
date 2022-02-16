from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    # firstname = db.Column(db.String(30), nullable=False)
    # lastname = db.Column(db.String(30), nullable=False)
    # patronymic = db.Column(db.String(40), nullable=False)
    #
    # phone = db.Column(db.String(11))
    # email = db.Column(db.String(100))
    # sex = db.Column(db.String(1), nullable=False, default="М")
    # birthday = db.Column(db.Date)

    def __repr__(self):
        return '<User %r>' % self.username

from . import views
