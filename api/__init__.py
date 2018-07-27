from .common import common_blueprint, common_api
from .problem import problem_blueprint, problem_api
from .contest import contest_blueprint, contest_api

blueprint_list = [common_blueprint, problem_blueprint, contest_blueprint]
api_list = [common_api, problem_api, contest_api]
