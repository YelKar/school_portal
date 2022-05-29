"""All routes with forms

routes for:
    Login form
    Register form

user authorization and creating accounts
"""
from flask import render_template, url_for, redirect, request
from flask_sqlalchemy import BaseQuery

# import configuration and db models
from application import application, login_manager, db
from application.config import my_resp
from application.database import Users, UserInfo, Publications

# import all for authorization
from flask_login import login_user, logout_user, current_user
from application.userLogin import UserLogin
from application.forms import LoginForm, RegisterForm, NewAdForm, NewEventForm

from werkzeug.security import generate_password_hash
from werkzeug.wrappers import Response
from colorama import Fore, Style
from datetime import datetime


@login_manager.user_loader
def load_user(user_id) -> UserLogin:
    """Load user and return object for currant_user

    :param user_id:
    :return: UserLogin
    """
    return UserLogin(user_id)


@application.route("/register", methods=["GET", "POST"])
def register() -> str or Response:
    """Add user to db

    render form from RegisterForm object

    get form data if form passed validation, generate password hash and add data to the DataBase
    :return: str (HTML_Template) or Response
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

        # saving data
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("accounts/register.html", title="Регистрация", form=form)


@application.route("/login", methods=["GET", "POST"])
def login() -> str or Response:
    """Log in user

    if user is logged in, he is redirected to the profile

    if user is not logged, render the form from RegisterForm object
    after filling out the form, authorized user

    :return: str (HTML_Template) or Response
    """
    if current_user.is_authenticated:  # if user is authorized, he is redirected to the profile
        return redirect(url_for("profile"))
    else:
        form = LoginForm()   # create form object

        if form.validate_on_submit():   # if form passed validation
            user: Users = Users.query.filter(form.username.data == Users.username).first()  # get user from database
            user_login = UserLogin(user)

            # print info about authorization
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT
                  + my_resp(f' User "{user.username}" was logged in')
                  + Style.RESET_ALL)

            login_user(user_login, remember=form.remember.data)    # user authorization
            next_page = request.args.get("next")
            return redirect(next_page or url_for("profile"))
    return render_template("accounts/login.html", form=form, title="Авторизация")


@application.route("/logout")
def logout() -> Response:
    """logout

    logging out user and redirecting to main page
    :return: Response
    """
    logout_user()
    return redirect(url_for("index"))


# Publications
@application.route('/new_ad', methods=['GET', 'POST'])
def new_ad() -> str or Response:
    """Create ad

    Rendering form for creating ad

    getting form data if form passed validation
    adding data to database

    :return: str (HTML_Template) or Response
    """
    form = NewAdForm()
    if form.validate_on_submit():
        post = Publications(
            user_id=current_user.id,
            header=form.header.data,
            post=form.text.data,
            type="ad",
            publication_date=datetime.now().timestamp()
        )

        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("publications/new_ad.html", form=form, title="Новое объявление")


@application.route('/new_event', methods=["GET", "POST"])
def new_event():
    """Create event

    Rendering form for creating event

    getting form data if form passed validation
    adding data to database

    :return: str (HTML_Template) or Response
    """
    form = NewEventForm()
    if form.validate_on_submit():
        post = Publications(
            user_id=current_user.id,
            header=form.header.data,
            post=form.text.data,
            date=form.datetime.data.timestamp(),
            type="event",
            publication_date=datetime.now().timestamp()
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("publications/new_event.html", form=form, title="Новое событие")


@application.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id: int):
    post: Publications = Publications.query.filter_by(id=post_id).first()
    if post.user_id != current_user.id:
        return redirect(url_for("login"))
    form: NewEventForm or NewAdForm = {
        "event": NewEventForm,
        "ad": NewAdForm,
    }[post.type]()

    if form.validate_on_submit():
        post.header = form.header.data
        post.post = form.text.data
        if post.type == "event":
            post.date = form.datetime.data.timestamp()
        db.session.commit()
        return redirect(url_for("my_posts"))
    form.header.data = post.header
    form.text.data = post.post
    if post.type == "event":
        form.datetime.data = datetime.fromtimestamp(post.date)
    return render_template(f"publications/new_{post.type}.html", form=form, title="Новое событие")


@application.route("/delete/<int:post_id>", methods=["GET", "POST"])
def del_post(post_id: int):
    post: BaseQuery = Publications.query.filter_by(id=post_id)
    if post.first().user_id == current_user.id:
        post.delete()
        db.session.commit()
    else:
        return redirect(url_for("login"))
    return redirect(url_for("index"))
