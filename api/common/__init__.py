from flask import Blueprint
from flask_restful import Api
from .ping import LoginPing
from .ping import Ping

common_blueprint = Blueprint('ping_blueprint', __name__)
common_api = Api(common_blueprint, prefix="/api")

common_api.add_resource(Ping, '/ping')
common_api.add_resource(LoginPing, '/login_ping')
