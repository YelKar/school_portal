from app import app
from .views import base
from flask import render_template, url_for, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from app import Users, db
from app.forms import *


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        u = Users(username=form.username.data, password=password_hash, email=form.email.data)
        db.session.add(u)
        db.session.flush()

        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", base=base, title="Регистрация", form=form)


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

