from app import app, login_manager
from app.userLogin import UserLogin
from app.config import my_resp
from flask_login import login_user, logout_user, current_user
from .views import base
from flask import render_template, url_for, redirect, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.wrappers import Response
from app import db
from app.database import Users, UserInfo
from app.forms import *
from colorama import Fore, Style


@login_manager.user_loader
def load_user(user_id) -> UserLogin:
    return UserLogin(user_id)


@app.route("/register", methods=["GET", "POST"])
def register() -> str or Response:
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
        # adding row to database
        db.session.add(u)
        db.session.flush()

        # adding info about user
        ui = UserInfo(
            user_id=u.id,
            sex=form.sex.data == "М",
        )
        db.session.add(ui)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("accounts/register.html", base=base, title="Регистрация", form=form)


@app.route("/login", methods=["GET", "POST"])
def login() -> str or Response:
    """Log in user

    if user is logged in, he is redirected to the profile

    if user is not logged, render the form from RegisterForm object
    after filling out the form, authorized user

    :return: str (HTML_Template)
    """
    if current_user.is_authenticated:  # if user is authorized, he is redirected to the profile
        return redirect(url_for("profile"))
    else:
        form = LoginForm()   # create form object
        if form.validate_on_submit():   # if form passed validation
            user: Users = Users.query.filter(form.username.data == Users.username).first()  # get user from database
            user_login = UserLogin(user)
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT
                  + my_resp(f' User "{user.username}" was logged in')
                  + Style.RESET_ALL)

            login_user(user_login, remember=form.remember.data)    # user authorization

            return redirect(url_for("profile"))
    return render_template("accounts/login.html", base=base, form=form)


@app.route("/logout")
def logout() -> Response:
    """logout

    logging out user and redirecting to main page
    :return:
    """
    logout_user()
    return redirect(url_for("index"))
