"""Creating admin class

"""
from flask import redirect, url_for
from app import admin, db
from app.database import Users, UserInfo
from flask_login import current_user

from flask_admin.contrib.sqla import ModelView
from flask_admin import expose, BaseView
from flask_admin.menu import MenuLink


class AdminView(ModelView):
    """Object for view database models

    checking user role and view database model
    """
    def __init__(self, *args, column_list=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._list_columns = column_list or self._list_columns

    def is_accessible(self) -> bool:
        """check user role and return True if user is admin"""
        return current_user.is_authenticated and current_user.is_admin

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

UserInfo_column_list = (
    ("user_id", "ID"),
    ("birthdate", "Дата рождения"),
    ("sex", "Пол"),
    ("many_children", "Многодетность"),
    ("fathers_lastname", "Фамилия отца"),
    ("fathers_firstname", "Имя отца"),
    ("fathers_patronymic", "Отчество отца"),
    ("mothers_lastname", "Фамилия матери"),
    ("mothers_firstname", "Имя матери"),
    ("mothers_patronymic", "Отчество матери"),
)

admin.add_link(MenuLink(name="На главную страницу", url="/"))

admin.add_view(AdminView(Users, db.session,
                         name="Пользователи",
                         column_list=Users_column_list
                         ))

admin.add_view(AdminView(UserInfo, db.session,
                         name="Информация о пользователях",
                         column_list=UserInfo_column_list
                         ))
