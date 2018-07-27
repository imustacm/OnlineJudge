from flask import Blueprint
from flask_restful import Api
from .ping import LoginPing
from .ping import Ping

common_blueprint = Blueprint('ping_blueprint', __name__)
common_api = Api(common_blueprint, prefix="/api")

common_api.add_resource(Ping, Ping.url)
common_api.add_resource(LoginPing, LoginPing.url)

from .cerlert_test import C, B

common_api.add_resource(C, C.url)
common_api.add_resource(B, B.url)
