# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from instance import config
# after existing third-party imports
from flask_migrate import Migrate

# after existing third-party imports
from flask_login import LoginManager

# after the db variable initialization
login_manager = LoginManager()


# local imports
#from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(app_config[config_name])
    app.config.from_object(config)
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    from app import models
    return app