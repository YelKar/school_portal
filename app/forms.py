from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField("Логин: *", validators=[DataRequired()],
                           render_kw={"placeholder": "Введите имя пользователя"})
    password = PasswordField("Пароль: *", validators=[Length(min=8)], render_kw={"placeholder": "Введите пароль"})
    submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
    username = StringField("Логин: *", validators=[DataRequired(), Length(min=2, max=30)],
                           render_kw={"placeholder": "Придумайте имя пользователя"})
    password = StringField("Пароль: *", validators=[Length(min=6)],
                           render_kw={"placeholder": "Придумайте пароль"})
    email = EmailField("Email", validators=[Email()],
                       render_kw={"placeholder": "your@ema.il"})
    submit = SubmitField("Создать")

