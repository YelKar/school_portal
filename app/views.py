from app import app
from flask import render_template, abort
from werkzeug.exceptions import HTTPException
from flask_login import login_required


base = "base/base.html"  # Путь к базе данных


# main page
@app.route('/')
def index() -> str:
    """
    render html template from "index.html"
    :return: str
    """

    return render_template(
        "index.html",
        title="1060",
        base=base
    )


if app.debug:
    @app.route("/abort-<int:error_code>")
    def abort_error(error_code: int) -> None:
        """
        cause <response error_code> (400 <= error_code <= 505)
        :param error_code: int
        :return: None
        """
        abort(error_code)


@app.route("/profile")
@login_required
def profile():
    """
    show profile page if user is authorize
    else redirect to <login_manager.login_view> and show message <login_manager.login_message>
    :return: str (HTML_Template)
    """
    return render_template("profile/profile.html", base=base)


@app.route('/profile/info')
@login_required
def profile_info():
    """Table with information about user"""
    return render_template("profile/profile_info.html", base=base)


@app.errorhandler(HTTPException)
def error_requests(e: HTTPException):
    """
    catches error responses and shows its page
    :param e: HTTPException
    :return: str (HTML_Template)
    """
    return render_template(
        "errors.html",
        base=base,
        error=e,
        title=e.name
    ), e.code


from . import docs_views
from . import form_views
