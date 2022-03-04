from app import app, login_manager
from app.userLogin import UserLogin
from flask_login import login_user, login_required, logout_user, current_user
from .views import base
from flask import render_template, url_for, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.database import Users
from app.forms import *


login_manager.login_view = "login"
login_manager.login_message = "Вы не авторизованы"


@login_manager.user_loader
def load_user(user_id):
    return UserLogin().from_db(user_id)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()   # create form object
    if form.validate_on_submit():    # if form passed validation
        # coding password
        password_hash = generate_password_hash(form.password.data)
        # get data and create row for database
        u = Users(username=form.username.data, password=password_hash,
                  email=form.email.data,
                  firstname=form.firstname.data, lastname=form.lastname.data, patronymic=form.patronymic.data,
                  sex=form.sex.data, classroom=str(form.classroom.data)+form.classletter.data)
        # add row to database
        db.session.add(u)
        db.session.flush()
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", base=base, title="Регистрация", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:  # if user is authorized, he is redirected to the profile
        return redirect(url_for("profile"))
    else:
        form = LoginForm()   # create form object
        if form.validate_on_submit():   # if form passed validation
            user = Users.query.filter(form.username.data == Users.username).first()  # get user from database
            user_login = UserLogin().create(user)
            login_user(user_login)    # user authorization
            return redirect(url_for("profile"))
    return render_template("login.html", base=base, form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
