from app import app
from .views import base
from flask import render_template, url_for, session, redirect
from app.forms import *


@app.route("/login", methods=["GET", "POST"])
def login():
    if "userLogged" in session:
        return redirect(url_for("profile", username=session["userLogged"]))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            print(form.username.data)
            print(form.password.data)
            session["userLogged"] = form.username.data
            return redirect(url_for("profile", username=session["userLogged"]))
    return render_template("login.html", base=base, form=form)


@app.route("/profile/<username>")
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        return redirect(url_for("login"))
    return render_template("profile.html", base=base, username=username)


@app.route("/logout")
def logout():
    session.pop("userLogged")
    return redirect("index")

