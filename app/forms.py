"""Creating form objects"""
from app.database import Users

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, TextAreaField,\
    SubmitField, SelectField, BooleanField, DateTimeLocalField
from wtforms.validators import DataRequired, Length,\
    Email, EqualTo, \
    NumberRange, ValidationError

from werkzeug.security import check_password_hash

import datetime as dt


class LoginForm(FlaskForm):
    """Creating form for authorization

    creating username, password and submit fields
    checking user in database
    """
    username = StringField("Логин: *", validators=[DataRequired()],
                           render_kw={"placeholder": "Введите имя пользователя"})
    password = PasswordField("Пароль: *", validators=[Length(min=6)], render_kw={"placeholder": "Введите пароль"})

    remember = BooleanField("Запомнить")

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
        """checking if email is used"""
        emails = [user.email.lower() if user.email else user.email for user in Users.query.all()]
        if field.data.lower() in emails:
            raise ValidationError("Такой email уже зарегистрирован")

    def validate_firstname(self, field: StringField):
        """validate name

        checking if first letter is upper,
        other letters is lower and
        digits not in name
        """
        if not field.data.isalpha():
            raise ValidationError("Имя должно состоять из букв")
        elif not (field.data[0].isupper() and field.data[1:].islower()):
            raise ValidationError("Имя должно начинаться с большой буквы")

    def validate_lastname(self, field: StringField):
        """validate lastname

        checking if first letter is upper,
        other letters is lower and
        digits not in lastname
        """
        if not field.data.isalpha():
            raise ValidationError("Фамилия должна состоять из букв")
        elif not (field.data[0].isupper() and field.data[1:].islower()):
            raise ValidationError("Фамилия должна начинаться с большой буквы")

    def validate_patronymic(self, field: StringField):
        """validate patronymic

        checking if first letter is upper,
        other letters is lower and
        digits not in patronymic
        """
        if not field.data.isalpha():
            raise ValidationError("Отчество должно состоять из букв")
        elif not (field.data[0].isupper() and field.data[1:].islower()):
            raise ValidationError("Отчество должно начинаться с большой буквы")

    username = StringField("Логин: *", validators=[DataRequired(), Length(min=2, max=30)],
                           render_kw={"placeholder": "Ivanious"})
    password = PasswordField("Пароль: *", validators=[DataRequired(), Length(min=6),
                                                      EqualTo("repeat_password", "Пароли не равны")],
                             render_kw={"placeholder": "••••••"})
    repeat_password = PasswordField("Повторите пароль: *",
                                    validators=[DataRequired()],
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


class NewAdForm(FlaskForm):
    """Form for creating ad"""
    header = StringField(validators=[DataRequired()], render_kw={"placeholder": "Заголовок"})
    text = TextAreaField(validators=[DataRequired()], render_kw={"placeholder": "Текст объявления"})

    submit = SubmitField("Опубликовать")


class NewEventForm(NewAdForm):
    """From for creating event"""
    def validate_datetime(self, field: DateTimeLocalField):
        try:
            if field.data.timestamp() < dt.datetime.now().timestamp():
                raise ValidationError(f"Укажите время больше {dt.datetime.now().strftime('%H:%M %d.%m.%Y')}")
        except OSError:
            raise ValidationError(
                f"Укажите время от {dt.datetime.fromtimestamp(86400).strftime('%H:%M %d.%m.%Y')}"
                f" до {dt.datetime.fromtimestamp(32536789199).strftime('%H:%M %d.%m.%Y')}"
            )
    datetime = DateTimeLocalField(validators=[DataRequired()], format="%Y-%m-%dT%H:%M")
