# -*- utf-8 -*-
from flask_restful import Resource

from models.users import Users
from utils.data import Data


class RankNumber(Resource):
    """
    评判状态数量
    """

    # TODO: cache
    api_url = '/rank_num'
    public_api = True

    @staticmethod
    def get():
        numbers = Users.query.order_by(Users.id).filter_by(visible=True).count()
        data = Data(data={"count": numbers}, status=200)
        return data.to_response()
