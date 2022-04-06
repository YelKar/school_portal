"""creating current_user object

"""
from flask import current_app
from app.database import Users
from flask_login import UserMixin, current_user
from functools import wraps


class UserLogin(UserMixin):
    """current_user

    """
    def __init__(self, user: Users or int or str):
        if type(user) != int and type(user) != str:
            self.user = user
        else:
            self.user = Users.query.filter_by(id=user).first()

        self.is_admin = self.user.role == "admin"
        self.is_student = self.user.role == "student"
        self.id = self.user.id

    def __repr__(self):
        return self.user.username

    def update(self):
        """getting up-to-date data from the database"""
        self.__init__(Users.query.filter_by(id=self.user.id).first())


def is_role(role):
    """checking is current_user.user.role == role

    :return:
    """
    def wrapper(func):
        """Decorate route
        :param func:
        :return:
        """
        @wraps(func)
        def decorated_view(*args, **kwargs):
            """checking if user role is <role>"""
            if current_user.user.role == role:
                return func(*args, **kwargs)
            return current_app.login_manager.unauthorized()
        return decorated_view
    return wrapper
