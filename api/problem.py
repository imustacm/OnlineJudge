from flask_restful import Resource

from models.problem import Problem
from utils.data import Data


class GetProblemById(Resource):
    @staticmethod
    def get(problem_id):
        results = Problem.query.filter_by(id=problem_id).all()
        if len(results) == 0:
            return Data(data=[], status=404, message='not found message about `%s`' % problem_id).to_response()
        schools = [item.to_dict() for item in results]
        data = Data(data=schools, status=200)
        return data.to_response()
