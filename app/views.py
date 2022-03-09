from app import app, db
from flask import render_template, url_for, \
    request, flash, abort, session, make_response, Response
from werkzeug.exceptions import HTTPException
from flask_login import login_required, current_user
from app.database import Users


base = "base.html"


@app.route('/')
def index():
    title = "1060"
    return render_template("index.html", title=title, base=base)


@app.route("/abort-<int:error_code>")
def abort_error(error_code):
    abort(error_code)
    return f"{error_code}"


@app.route("/profile")
@login_required
def profile():
    return render_template("profile/profile.html", base=base)


@app.route('/profile/info')
def profile_info():
    return render_template("profile/profile_info.html", base=base)


@app.route('/chose_documents')
def chose_documents():
    return render_template("documents/chose_documents.html", base=base, users=Users, db=db)


@app.route("/print")
def print_document():
    return render_template("print.html", base=base)


@app.errorhandler(HTTPException)
def error_requests(e: HTTPException):
    return render_template("errors.html", base=base,
                           error=e, title=e.name), e.code


@app.route('/docs-<name>')
def docs(name):
    return render_template("documents/show_docs.html", name=name,
                           base=base)


from . import form_views
