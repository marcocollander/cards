from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), Email()])
    password = PasswordField("Hasło: ", validators=[DataRequired()])
    submit = SubmitField("Zaloguj się")


class RegisterForm(FlaskForm):
    name = StringField("Imię: ", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired(),Email()])
    password = PasswordField("Hasło:", validators=[DataRequired()])
    submit = SubmitField("Zarejestruj się")