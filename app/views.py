from app import app
from flask import render_template, url_for, request, flash


base = "base.html"


@app.route('/')
@app.route('/index')
@app.route('/main')
def index():
    title = "1060"
    return render_template("index.html", title=title, base=base)


@app.route("/print")
def print_document():
    return render_template("print.html", base=base)
