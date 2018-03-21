from flask import request
from flask_restful import Resource
from utils.data import Data
from auth import login_require
import json


class Ping(Resource):
    @staticmethod
    def get():
        data = Data(message="It's OK, you get me", data=request.args, status=200)
        return data.to_response()

    @staticmethod
    def post():
        echo = json.loads(request.get_data())
        data = Data(message="It's OK, you post me", data=echo, status=200)
        return data.to_response()


class LoginPing(Resource):
    method_decorators = [login_require]

    @staticmethod
    def get():
        data = Data(data=["It's OK, you already login", request.args], status=200)
        return data.to_response()

    @staticmethod
    def post():
        echo = json.loads(request.get_data())
        data = Data(message="It's OK, you already login", data=echo, status=200)
        return data.to_response()
