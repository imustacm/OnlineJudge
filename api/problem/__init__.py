from flask import Blueprint
from flask_restful import Api
from .problem import GetProblemById
from .problem_list import GetProblemList
from .problem_number import CountProblemNumber

problem_blueprint = Blueprint('problem_blueprint', __name__)
problem_api = Api(problem_blueprint, prefix="/api/problems")

problem_api.add_resource(GetProblemById, '/problem')
problem_api.add_resource(GetProblemList, '/problem_list')
problem_api.add_resource(CountProblemNumber, '/problem_num')
