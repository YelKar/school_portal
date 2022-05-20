"""creating current_user object

"""
from application.database import Users
from flask_login import UserMixin


class UserLogin(UserMixin):
    """current_user

    """
    def __init__(self, user: Users or int or str):
        if type(user) != int and type(user) != str:
            self.user = user
        else:
            self.user = Users.query.filter_by(id=user).first()

        self.is_admin = "admin" in self.user.role
        self.is_student = "student" in self.user.role
        self.is_teacher = "teacher" in self.user.role
        self.id = self.user.id

    def __repr__(self):
        return self.user.username

    def update(self):
        """getting up-to-date data from the database"""
        self.__init__(Users.query.filter_by(id=self.user.id).first())
