# -*- utf-8 -*-
from flask import request
from werkzeug.exceptions import BadRequestKeyError
from flask_restful import Resource

from models.problem import Problem
from utils.data import Data


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
