from flask import Blueprint
from flask_restful import Api, Resource

from .ping import Ping
from .ping import LoginPing
from .problem import GetProblemById
from .problem import GetProblemList
from .problem import CountProblemNumber
from .auth import Login
from .captcha_code import Captcha
from .contest import *
import api.contest

api_module_list = [api.contest]

ping_blueprint = Blueprint('ping_blueprint', __name__)
ping_api = Api(ping_blueprint, prefix="/api")
account_blueprint = Blueprint('auth_blueprint', __name__)
account_api = Api(account_blueprint, prefix="/api/account")
problem_blueprint = Blueprint('problem_blueprint', __name__)
problem_api = Api(problem_blueprint, prefix="/api/problems")
captcha_blueprint = Blueprint('captcha_blueprint', __name__)
captcha_api = Api(captcha_blueprint, prefix="/api/captcha")
contest_blueprint = Blueprint('contest_blueprint', __name__)
contest_api = Api(contest_blueprint, prefix="/api/contests")

api_map = {
    api.contest: contest_api
}
ping_api.add_resource(Ping, '/ping')
ping_api.add_resource(LoginPing, '/login_ping')

account_api.add_resource(Login, '/login')

problem_api.add_resource(GetProblemById, '/problem')
problem_api.add_resource(GetProblemList, '/problem_list')
problem_api.add_resource(CountProblemNumber, '/problem_num')

captcha_api.add_resource(Captcha, '/get')

for api_module in api_module_list:
    for item in dir(api_module):
        api_obj = getattr(api.contest, item)
        if hasattr(api_obj, 'public_api') and getattr(api_obj, 'public_api'):
            api_map[api.contest].add_resource(api_obj, api_obj.api_url)
            # contest_api.add_resource(api_obj, api_obj.api_url)
