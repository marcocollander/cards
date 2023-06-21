# Aplikacja Flaska znajduje się w pakiecie app
# Konstruktor pakietu aplikacji
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Momment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    # from_object() to metoda obiektu
    # konfiguracji app.config Flaska
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app