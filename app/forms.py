from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Логин: *", validators=[DataRequired()],
                           render_kw={"placeholder": "Введите имя пользователя"})
    password = PasswordField("Пароль: *", validators=[Length(min=8)], render_kw={"placeholder": "Введите пароль"})
    submit = SubmitField("Войти")
