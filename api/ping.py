from flask import request, jsonify
from flask_restful import Resource

from utils.data import Data
from auth import login_require


class Ping(Resource):
    @staticmethod
    def get():
        data = Data(data=["It's OK, you get me", request.args], status=200)
        return data.to_response()

    @staticmethod
    def post():
        data = Data(data=["It's OK, you post me", request.get_json()], status=200)
        return data.to_response()


class LoginPing(Resource):
    method_decorators = [login_require]

    @staticmethod
    def get():
        data = Data(data=["It's OK, you already login", request.args], status=200)
        return data.to_response()

    @staticmethod
    def post():
        data = Data(data=["It's OK, you already login", request.get_json()], status=200)
        return data.to_response()
