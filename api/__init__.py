from flask import Blueprint
from flask_restful import Api, Resource

from .ping import Ping
from .ping import LoginPing
from .problem import GetProblemById
from .problem import GetProblemList
from .problem import CountProblemNumber
from .captcha_code import Captcha
from .contest import *
import api.contest
from .submission import SubmissionNumber
from .rank import RankNumber
from .user import Register
from .user import Login
from .user import Logout

api_module_list = [api.contest]

ping_blueprint = Blueprint('ping_blueprint', __name__)
ping_api = Api(ping_blueprint, prefix="/api")
problem_blueprint = Blueprint('problem_blueprint', __name__)
problem_api = Api(problem_blueprint, prefix="/api/problems")
captcha_blueprint = Blueprint('captcha_blueprint', __name__)
captcha_api = Api(captcha_blueprint, prefix="/api/captcha")
contest_blueprint = Blueprint('contest_blueprint', __name__)
contest_api = Api(contest_blueprint, prefix="/api/contests")
submission_blueprint = Blueprint('submission_blueprint', __name__)
submission_api = Api(submission_blueprint, prefix="/api/status")
rank_blueprint = Blueprint('rank_blueprint', __name__)
rank_api = Api(rank_blueprint, prefix='/api/rank')
user_blueprint = Blueprint('user_blueprint', __name__)
user_api = Api(user_blueprint, prefix='/api/user')

api_map = {
    api.contest: contest_api
}
ping_api.add_resource(Ping, '/ping')
ping_api.add_resource(LoginPing, '/login_ping')

user_api.add_resource(Register, '/register')
user_api.add_resource(Login, '/login')
user_api.add_resource(Logout, '/logout')

problem_api.add_resource(GetProblemById, '/problem')
problem_api.add_resource(GetProblemList, '/problem_list')
problem_api.add_resource(CountProblemNumber, '/problem_num')

submission_api.add_resource(SubmissionNumber, '/status_num')

rank_api.add_resource(RankNumber, '/rank_num')

captcha_api.add_resource(Captcha, '/get')

for api_module in api_module_list:
    for item in dir(api_module):
        api_obj = getattr(api.contest, item)
        if hasattr(api_obj, 'public_api') and getattr(api_obj, 'public_api'):
            api_map[api.contest].add_resource(api_obj, api_obj.api_url)
            # contest_api.add_resource(api_obj, api_obj.api_url)
