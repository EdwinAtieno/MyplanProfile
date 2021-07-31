# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from instance import config
# after existing third-party imports
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
# after existing third-party imports
from flask_login import LoginManager

# after the db variable initialization
login_manager = LoginManager()

# after existing third-party imports
from flask_bootstrap import Bootstrap
# local imports
#from config import app_config

# db variable initialization
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(app_config[config_name])
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    Bootstrap(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db, ma)



    from app import models

    from .profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)



    return app