"""Setting configuration for app"""
import os
from flask import request
from time import strftime
from functools import wraps
from flask import current_app
from flask_login import current_user, login_required
from flask_admin import AdminIndexView, expose


class Config(object):
    """Configuration object for app"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or "any_key"  # Creating secret key for forms
    DEBUG = True  # Activating debug mode
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.db"  # route to database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = "solar"


def my_resp(text: str = ""):
    return f'{request.remote_addr} - - {strftime("[%d/%b/%Y %H:%M:%S]")} {text}'


def is_role(role: str):
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
            if current_user.is_authenticated and not set(current_user.user.role.split()).isdisjoint(role.split()):
                return func(*args, **kwargs)
            return current_app.login_manager.unauthorized()
        return decorated_view
    return wrapper


class IndexView(AdminIndexView):
    @expose()
    @is_role("admin")
    @login_required
    def index(self):
        return self.render(self._template)
