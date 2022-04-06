"""creating SQlite models


"""
from app import db


class Users(db.Model):
    """Main database for users"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(500), nullable=False)

    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(50))
    patronymic = db.Column(db.String(50))

    classroom = db.Column(db.String(3), nullable=False)

    email = db.Column(db.String(100), unique=True)

    role = db.Column(db.String(10), nullable=False, default="student")

    info = db.relationship("UserInfo", backref="users", uselist=False)

    def __repr__(self):
        return f"<Users {self.id}>"


class UserInfo(db.Model):
    """Database for userinfo"""

    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    sex = db.Column(db.Boolean, nullable=False)
    birthdate = db.Column(db.Integer)
    many_children = db.Column(db.Boolean)

    fathers_firstname = db.Column(db.String(30))
    fathers_lastname = db.Column(db.String(50))
    fathers_patronymic = db.Column(db.String(50))

    mothers_firstname = db.Column(db.String(30))
    mothers_lastname = db.Column(db.String(50))
    mothers_patronymic = db.Column(db.String(50))

    def __repr__(self):
        return f"<UserInfo {self.id} for {self.user_id}>"
