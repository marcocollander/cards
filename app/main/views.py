from datetime  import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import MainForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    if session.get('known'):
        message = f'Witaj ponownie {session.get("name")}'
    else:
        message = 'Możesz grać bez logowania lecz twoje wyniki nie będą zapisywane'
    return render_template('index.html', message=message)


