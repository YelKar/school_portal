from app import app, db
from flask import render_template, url_for, \
    request, flash, abort, session, make_response, Response
from werkzeug.exceptions import HTTPException
from flask_login import login_required, current_user
from app.database import Users


base = "base.html"  # Путь к базе данных


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
    return render_template("profile/profile_info.html", base=base)


@app.route('/chose/documents')
def chose_documents():
    """chose document to print

    if request method is POST goto chose_student
    else render form for chose document
    TODO создать форму для выбора документов
    :return: str (HTML_Template)
    """
    return render_template(
        "documents/chose_documents.html",
        base=base,
        users=Users,
        db=db
    )


@app.route('/chose/students', methods=['GET', 'POST'])
def chose_students():
    """chose students and goto print

    if request method is POST goto print
    else render form for chose students
    TODO Реализовать получение данных о выбранных пользователях
    TODO и переброску их на страницу печати
    TODO реализовать фильтры
    :return: str (HTML_Template)
    """
    if request.method == "POST":
        print(request.form)
    return render_template(
        "documents/chose_students.html",
        base=base,
        users=Users,
        db=db
    )


@app.route("/print")
def print_document():
    return render_template("documents/print.html", base=base, Users=Users)


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


@app.route('/docs-<name>')
def docs(name):
    return render_template("documents/show_docs.html", name=name,
                           base=base)


from . import form_views
