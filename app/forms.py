"""Creating form objects"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length,\
    Email, EqualTo, \
    NumberRange, ValidationError
from werkzeug.security import check_password_hash
from app import db
from app.database import Users


class LoginForm(FlaskForm):
    """Creating form for authorization

    creating username, password and submit fields
    checking user in database
    """
    username = StringField("Логин: *", validators=[DataRequired()],
                           render_kw={"placeholder": "Введите имя пользователя"})
    password = PasswordField("Пароль: *", validators=[Length(min=6)], render_kw={"placeholder": "Введите пароль"})

    def validate_user(self, _: SubmitField) -> ValidationError or None:
        """checking, if user in db

        get user from db
        "select * from users where username = self.username.data" limit 1;

        and check password
        :param _: SubmitField
        :return: ValidationError or None
        """
        u = Users.query.filter(Users.username == self.username.data).first()
        if u:
            if check_password_hash(u.password, self.password.data):
                return
        raise ValidationError("Неверный логин или пароль")
    submit = SubmitField("Войти", validators=[validate_user])


class RegisterForm(FlaskForm):
    """creating form for registration

    """
    def validate_username(self, field) -> ValidationError or None:
        """validation username

        checking, is username in db
        if username in db raise "Такой логин уже есть"

        :param field:
        :raise: ValidationError
        """
        usernames = [user.username for user in Users.query.all()]
        if field.data in usernames:
            raise ValidationError("Такой логин уже есть")

    def validate_email(self, field) -> ValidationError or None:
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

    email = EmailField("Email", validators=[Email(), DataRequired()],
                       render_kw={"placeholder": "your@ema.il"})

    firstname = StringField("Имя: *", validators=[DataRequired()],
                            render_kw={"placeholder": "Иван"})
    lastname = StringField("Фамилия: *", validators=[DataRequired()],
                           render_kw={"placeholder": "Иванов"})
    patronymic = StringField("Отчество: *", validators=[DataRequired()],
                             render_kw={"placeholder": "Иванович"})

    sex = SelectField("Пол: *", choices=["М", "Ж"])
    classroom = IntegerField("Класс: ",
                             validators=[
                                 NumberRange(max=11, min=1, message="Неверный класс")
                             ],
                             default=1,
                             render_kw={"placeholder": "1-11"})
    classletter = SelectField("Буква: ", choices=["н", "о", "п"])

    submit = SubmitField("Создать")
