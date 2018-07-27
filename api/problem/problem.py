# -*- utf-8 -*-
from flask import request
from werkzeug.exceptions import BadRequestKeyError
from flask_restful import Resource

from models.problem import Problem
from utils.data import Data


class GetProblemById(Resource):
    @staticmethod
    def get():
        try:
            problem_id = int(request.args['id'])
        except (BadRequestKeyError, ValueError):
            data = Data(message='Invalid value of problem_id', status=422)
            return data.to_response()
        result = Problem.query.filter_by(id=problem_id).first()
        if result is None:
            return Data(data=[], status=404, message='not found message about `%s`' % problem_id).to_response()
        problem = result.to_dict()
        data = Data(data=problem, status=200)
        return data.to_response()
