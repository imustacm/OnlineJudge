from flask_restful import Resource

from utils.data import Data


class Ping(Resource):
    @staticmethod
    def get():
        data = Data(data="It's OK", status=200)
        return data.to_response()
