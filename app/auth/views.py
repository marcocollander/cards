from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegisterForm


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.arg.get('next')
            if next is None or not next.startswitch('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Nieprawidłowy email lub hasło')
    return render_template( "auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Zostałeś wylogowany')
    return redirect(url_for('main.index'))


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Możesz się zalogować.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
    
