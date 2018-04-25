from flask import Blueprint
from flask_restful import Api

from .ping import Ping
from .ping import LoginPing
from .problem import GetProblemById
from .problem import GetProblemList
from .auth import Login
from .captcha_code import Captcha

ping_blueprint = Blueprint('ping_blueprint', __name__)
ping_api = Api(ping_blueprint, prefix="/api")
ping_api.add_resource(Ping, '/ping')
ping_api.add_resource(LoginPing, '/login_ping')

account_blueprint = Blueprint('auth_blueprint', __name__)
account_api = Api(account_blueprint, prefix="/api/account")
account_api.add_resource(Login, '/login')

problem_blueprint = Blueprint('problem_blueprint', __name__)
problem_api = Api(problem_blueprint, prefix="/api/problems")
problem_api.add_resource(GetProblemById, '/id/<int:problem_id>')
problem_api.add_resource(GetProblemList, '/problem_list')

captcha_blueprint = Blueprint('captcha_blueprint', __name__)
captcha_api = Api(captcha_blueprint, prefix="/api/captcha")
captcha_api.add_resource(Captcha, '/get')
