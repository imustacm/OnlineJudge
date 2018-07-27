# -*- utf-8 -*-
from flask_restful import Resource

from models.contest import Contest
from utils.data import Data


class CountContestNumber(Resource):
    """
    竞赛数量
    """

    # TODO: cache
    api_url = '/contest_num'

    @staticmethod
    def get():
        numbers = Contest.query.order_by(Contest.id).filter_by(visible=True).count()
        data = Data(data={"count": numbers}, status=200)
        return data.to_response()
