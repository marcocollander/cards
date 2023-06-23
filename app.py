import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "<Role %r>" % self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "<User %r>" % self.username


class NameForm(FlaskForm):
    number_of_hits = StringField("Ilość trafień", validators=[DataRequired()])
    number_of_attempts = StringField("Ilość prób", validators=[DataRequired()])
    hit_percentage = StringField("Procent trafień", validators=[DataRequired()])
    submit = SubmitField("Wyślij")


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Hasło: ", validators=[DataRequired()])
    submit = SubmitField("Zaloguj się")


class RegisterForm(FlaskForm):
    name = StringField("Imię: ", validators=[DataRequired()])
    email = StringField("Email:", validators=[Email()])
    password = PasswordField("Hasło:", validators=[DataRequired()])
    submit = SubmitField("Zarejestruj się")


@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error():
    return render_template("500.html"), 500


@app.route('/', methods=['POST', 'GET'])
def index():
    if session.get('known'):
        message = f'Witaj ponownie {session.get("name")}'
    else:
        message = 'Możesz grać bez logowania lecz twoje wyniki nie będą zapisywane'
    return render_template('index.html', message=message)


@app.route("/log", methods=["GET", "POST"])
def login():
    message = session.get('message')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            print('Nie jesteś zarejestrowany')
            print('Zarejestruj się')
            session['known'] = False
            return redirect(url_for('register'))
        elif user.password == form.password.data:
            session["known"] = True
            session["name"] = user.username
            session['message'] = 'Jesteś zalogowany'
            print(f'Witaj {user.username}')
        else:
            session['message'] = 'Błędne dane logowanie'
            return redirect(url_for('login'))

        return redirect(url_for("index"))
    return render_template(
        "login.html",
        form=form, message=message
    )


@app.route("/out", methods=["GET", "POST"])
def outlogin():
    session['known'] = False
    session['message'] = 'Zostałeś wylogowany'
    return redirect(url_for("login"))


@app.route("/reg", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(
                username=form.name.data, email=form.email.data, password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        return redirect(url_for("login"))
    return render_template(
        "register.html",
        form=form,
    )


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
