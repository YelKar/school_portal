"""Creating admin class

"""
from flask import redirect, url_for
from app import admin, db
from app.database import Users, UserInfo
from flask_login import current_user

from flask_admin.contrib.sqla import ModelView
from flask_admin import expose, BaseView


class AdminView(ModelView):
    """Object for view database models

    checking user role and view database model
    """
    def __init__(self, *args, column_list=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._list_columns = column_list or self._list_columns

    def is_accessible(self) -> bool:
        """check user role and return True if user is admin"""
        return current_user.is_authenticated and current_user.user.role == "admin"

    def inaccessible_callback(self, name, **kwargs):
        """if user not authorized or he is not admin redirect his to main page"""
        if not self.is_accessible():
            return redirect(url_for('index'))

    page_size = 20
    column_exclude_list = ("password", "users")


class ToMainPage(BaseView):
    """creating button for index page"""
    @expose()
    def to_main(self):
        """redirect to main page"""
        return redirect(url_for("index"))


Users_column_list = (
    ("id", "ID"),
    ("username", "Логин"),
    ("lastname", "Фамилия"),
    ("firstname", "Имя"),
    ("patronymic", "Отчество"),
    ("classroom", "Класс"),
    ("email", "Email"),
    ("info.sex", "Пол"),
    ("info.birthdate", "Дата рождения"),
    ("info.many_children", "Многодетный"),
    ("role", "Роль")
)

admin.add_view(ToMainPage(name="На главную страницу"))

admin.add_view(AdminView(Users, db.session, name="Пользователи", column_list=Users_column_list))

ui = AdminView(UserInfo, db.session, name="Информация о пользователях")
ui._list_columns = [["user_id", "ID"]] + list(ui._list_columns)
admin.add_view(ui)
