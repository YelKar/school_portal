"""All routes for application

all routes for application
error handling
and importing other routes
"""
from application import application, db
from application.database import Users, Publications
from flask import render_template, abort
from flask_login import login_required
from werkzeug.exceptions import HTTPException


from . import docs_views
from . import form_views


# main page
@application.route('/')
def index() -> str:
    """
    render html template from "index.html"
    :return: str
    """
    return render_template(
        "index.html",
        title="Школа 1060",
        db=db,
        users=Users,
        posts=Publications
    )


if application.debug:
    @application.route("/abort-<int:error_code>")
    def abort_error(error_code: int) -> None:
        """
        cause <response error_code> (400 <= error_code <= 505)
        :param error_code: int
        :return: None
        """
        abort(error_code)

    @application.route("/test")
    def test_view():
        return render_template("test.html")


@application.route("/profile")
@login_required
def profile():
    """
    show profile page if user is authorize
    else redirect to <login_manager.login_view> and show message <login_manager.login_message>
    :return: str (HTML_Template)
    """
    return render_template("profile/profile.html", title="Профиль")


@application.route('/profile/info')
@login_required
def profile_info():
    """Table with information about user"""
    return render_template("profile/profile_info.html", title="Информация о пользователе")


@application.route("/new")
def new_post():
    """Rendering page with a selection of post templates"""
    return render_template("publications/new.html", title="Новая публикация")


@application.route('/my_posts')
def my_posts():
    """Rendering page with all publications that has been published by this user"""
    return render_template("profile/my_publications.html", title="Мои публикации", posts=Publications, users=Users)


@application.errorhandler(HTTPException)
def error_requests(e: HTTPException):
    """
    catches error responses and shows its page
    :param e: HTTPException
    :return: str (HTML_Template)
    """
    return render_template(
        "errors.html",
        error=e,
        title=e.name
    ), e.code
