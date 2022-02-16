from app import app
from flask import render_template, url_for, request, flash


base = "base.html"


@app.route('/')
def index():
    title = "1060"
    return render_template("index.html", title=title, base=base)
