from datetime  import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import MainForm, LoginForm, RegisterForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    if session.get('known'):
        message = f'Witaj ponownie {session.get("name")}'
    else:
        message = 'Możesz grać bez logowania lecz twoje wyniki nie będą zapisywane'
    return render_template('index.html', message=message)

@main.route("/log", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            session['known'] = False
            return redirect(url_for('.regist'))
        elif user.verify_password(form.password.data):
            session["known"] = True
            session["name"] = user.username
        else:
            return redirect(url_for('.login'))
        return redirect(url_for(".index"))
    return render_template(
        "login.html",
        form=form, name=session.get('name')
    )


@main.route("/out", methods=["GET", "POST"])
def outlogin():
    session['known'] = False
    session['message'] = 'Zostałeś wylogowany'
    return redirect(url_for(".login"))
    



@main.route("/reg", methods=["GET", "POST"])
def regist():
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
        return redirect(url_for(".login"))
    return render_template(
        "regist.html",
        form=form
    )
