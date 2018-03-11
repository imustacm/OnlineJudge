from flask import Flask
from config import config

from config import environment
from core.db import setup_db
from core.blueprints import setup_bluepoints


def create_app(config_name=environment):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    setup_db(app)
    setup_bluepoints(app)
    return app
