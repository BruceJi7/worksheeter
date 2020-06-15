from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
# from flask_moment import Moment
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
# mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    print('Configured as...')
    print(config[config_name])

    bootstrap.init_app(app)
    # mail.init_app(app) # Commented to remove mail functionality
    # moment.init_app(app) # Commented to remove moment functionality
    db.init_app(app)

    # Attach routes and custom error pages here wat
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
