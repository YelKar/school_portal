from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length,\
    Email, EqualTo, \
    NumberRange, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.database import Users


class LoginForm(FlaskForm):
    username = StringField("Логин: *", validators=[DataRequired()],
                           render_kw={"placeholder": "Введите имя пользователя"})
    password = PasswordField("Пароль: *", validators=[Length(min=6)], render_kw={"placeholder": "Введите пароль"})

    def validate_user(self, _):
        u = Users.query.filter(Users.username == self.username.data).all()
        if u:
            if check_password_hash(u[0].password, self.password.data):
                return
        raise ValidationError("Неверный логин или пароль")
    submit = SubmitField("Войти", validators=[validate_user])


class RegisterForm(FlaskForm):
    def validate_username(self, field):
        usernames = [user.username for user in Users.query.all()]
        if field.data in usernames:
            raise ValidationError("Такой логин уже есть")

    def validate_email(self, field):
        emails = [user.email for user in Users.query.all()]
        if field.data in emails:
            raise ValidationError("Такой email уже зарегистрирован")

    username = StringField("Логин: *", validators=[DataRequired(), Length(min=2, max=30)],
                           render_kw={"placeholder": "Ivanious"})
    password = PasswordField("Пароль: *", validators=[DataRequired(), Length(min=6)],
                             render_kw={"placeholder": "••••••"})
    repeat_password = PasswordField("Повторите пароль: *",
                                    validators=[DataRequired(), EqualTo("password", "Пароли не равны")],
                                    render_kw={"placeholder": "••••••"})

    firstname = StringField("Имя: *", validators=[DataRequired()],
                            render_kw={"placeholder": "Иван"})
    lastname = StringField("Фамилия: *", validators=[DataRequired()],
                           render_kw={"placeholder": "Иванов"})
    patronymic = StringField("Отчество: *", validators=[DataRequired()],
                             render_kw={"placeholder": "Иванович"})

    sex = SelectField("Пол: *", choices=["М", "Ж"])
    classroom = IntegerField("Класс: ", validators=[NumberRange(max=11, min=1, message="Неверный класс")],
                             default=1,
                             render_kw={"placeholder": "1-11"})
    classletter = SelectField("Буква: ", choices=["н", "о", "п"])

    email = EmailField("Email", validators=[Email(), DataRequired()],
                       render_kw={"placeholder": "your@ema.il"})
    submit = SubmitField("Создать")
