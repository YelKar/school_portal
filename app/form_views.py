from app import app, login_manager
from app.userLogin import UserLogin
from app.config import my_resp
from flask_login import login_user, login_required, logout_user, current_user
from .views import base
from flask import render_template, url_for, session, redirect, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.database import Users, UserInfo
from app.forms import *
from colorama import Fore, Style
from time import strftime


@login_manager.user_loader
def load_user(user_id) -> UserLogin:
    return UserLogin().from_db(user_id)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Add user to db

    render form from RegisterForm object

    get form data if form passed validation, generate password hash and add data to the DataBase
    :return: str (HTML_Template)
    """
    form = RegisterForm()   # create form object
    if form.validate_on_submit():    # if form passed validation
        # coding password
        password_hash = generate_password_hash(form.password.data)
        # get data and create row for database
        u = Users(
            username=form.username.data, password=password_hash,
            email=form.email.data,
            firstname=form.firstname.data, lastname=form.lastname.data, patronymic=form.patronymic.data,
            classroom=str(form.classroom.data) + form.classletter.data
        )
        ui = UserInfo(
            user_id=u.id,
            sex=form.sex.data,
        )
        # add row to database
        db.session.add(u)
        db.session.add(ui)
        db.session.flush()
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", base=base, title="Регистрация", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in user

    if user is logged in, he is redirected to the profile

    if user is not logged, render the form from RegisterForm object
    after filling out the form, authorized user

    :return: str (HTML_Template)
    """
    if current_user.is_authenticated:  # if user is authorized, he is redirected to the profile
        return redirect(url_for("profile"))
    else:
        form: FlaskForm = LoginForm()   # create form object
        if form.validate_on_submit():   # if form passed validation
            user: Users = Users.query.filter(form.username.data == Users.username).first()  # get user from database
            user_login = UserLogin().create(user)
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT
                  + my_resp(f' User "{user.username}" was logged in')
                  + Style.RESET_ALL)
            login_user(user_login)    # user authorization

            return redirect(url_for("profile"))
    return render_template("login.html", base=base, form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
