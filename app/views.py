from app import app
from flask import render_template, url_for, \
    request, flash, abort
from werkzeug.exceptions import HTTPException


base = "base.html"


@app.route('/')
def index():
    title = "1060"
    return render_template("index.html", title=title, base=base)


@app.route("/print")
def print_document():
    return render_template("print.html", base=base)


@app.route("/abort-<int:error_code>")
def abort_error(error_code):
    abort(error_code)
    return f"{error_code}"


@app.errorhandler(HTTPException)
def error_requests(e: HTTPException):
    return render_template("errors.html", base=base,
                           error=e, title=e.name), e.code


from . import form_views
