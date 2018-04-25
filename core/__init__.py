from flask import Flask

from config import config
from config import ENVIRONMENT
from core.db import setup_db
from core.blueprints import setup_bluepoints
from core.sentinel import setup_sentinel
from core.logger import setup_logging
from core.response import OJResponse
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def create_app(config_name=ENVIRONMENT):
    app = Flask(__name__, static_folder='../static', static_url_path='/assets')
    app.config.from_object(config[config_name])
    app.response_class = OJResponse
    setup_db(app)
    setup_bluepoints(app)
    setup_sentinel(app)
    setup_logging(app)
    return app
