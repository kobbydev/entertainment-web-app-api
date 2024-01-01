import os
from flask import Flask
from app.config import config_by_name
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from logging.config import dictConfig
import logging

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def create_app(config_name):
    app = Flask(__name__)
    # Configure Flask logging
    app.logger.setLevel(logging.INFO)  # Set log level to INFO
    handler = logging.FileHandler('app.log')  # Log to a file
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    app.logger.addHandler(handler)
    app.config.from_object(config_by_name[config_name])
    with app.app_context():
        Bcrypt(app)

    CORS(app)
    from app.routes import user_bp
    from app.routes import movies_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(movies_bp)
    return app


# bcrypt = Bcrypt(create_app(os.getenv('BOILERPLATE_ENV') or 'dev'))
