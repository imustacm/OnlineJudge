# -*- utf-8 -*-
from flask_restful import Resource

from models.submission import Submission
from utils.data import Data


class SubmissionNumber(Resource):
    """
    评判状态数量
    """

    # TODO: cache
    api_url = '/status_num'
    public_api = True

    @staticmethod
    def get():
        numbers = Submission.query.order_by(Submission.id).filter_by().count()
        data = Data(data={"count": numbers}, status=200)
        return data.to_response()
