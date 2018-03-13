from flask import Blueprint
from flask_restful import Api

from .ping import Ping
from .problem import GetProblemById
from .auth import Login

auth_blueprint = Blueprint('auth_blueprint', __name__)
auth_api = Api(auth_blueprint, prefix="/api/auth")
auth_api.add_resource(Login, '/login')

problem_blueprint = Blueprint('problem_blueprint', __name__)
problem_api = Api(problem_blueprint, prefix="/api/problems")
problem_api.add_resource(GetProblemById, '/id/<int:problem_id>')

ping_blueprint = Blueprint('ping_blueprint', __name__)
ping_api = Api(ping_blueprint, prefix="/api/ping")
ping_api.add_resource(Ping, '/')
