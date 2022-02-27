from app import db
from app.database import Users
from flask_login import UserMixin


class UserLogin(UserMixin):
    def __repr__(self):
        return self.__user.username

    def from_db(self, user_id):
        self.__user = Users.query.filter(Users.id == user_id).first()
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user.id)

    def get_user(self):
        return self.__user
