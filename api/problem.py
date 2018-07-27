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


class GetProblemList(Resource):
    @staticmethod
    def get():
        try:
            limit = int(request.args['limit'])
        except BadRequestKeyError:
            limit = 100
        except ValueError:
            data = Data(message='Invalid value of limit', status=422)
            return data.to_response()
        try:
            offset = int(request.args['offset'])
        except BadRequestKeyError:
            offset = 0
        except ValueError:
            data = Data(message='Invalid value of offset', status=422)
            return data.to_response()
        results = Problem.query.order_by(Problem.id).filter_by(visible=True).limit(limit).offset(offset).all()
        problem_list = []
        for item in results:
            problem = {
                "id": item.id,
                "title": item.title,
                "source": item.source,
                "submit_number": item.submit_number,
                "accepted_number": item.accepted_number
            }
            if item.submit_number == 0 or item.submit_number is None:
                problem['ac_rate'] = 0
            else:
                problem['ac_rate'] = item.accepted_number / item.submit_number
            problem_list.append(problem)
        data = Data(data=problem_list, status=200)
        return data.to_response()


class CountProblemNumber(Resource):
    """
    返回题目总数
    """

    # TODO: cache
    @staticmethod
    def get():
        numbers = Problem.query.order_by(Problem.id).filter_by(visible=True).count()
        data = Data(data={"count": numbers}, status=200)
        return data.to_response()
