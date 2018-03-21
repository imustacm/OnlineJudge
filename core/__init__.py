from flask import Flask

from config import config
from config import ENVIRONMENT
from core.db import setup_db
from core.blueprints import setup_bluepoints
from core.sentinel import setup_sentinel
from core.logger import setup_logging


def create_app(config_name=ENVIRONMENT):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    setup_db(app)
    setup_bluepoints(app)
    setup_sentinel(app)
    setup_logging(app)
    return app
