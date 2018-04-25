from flask import request
from flask_restful import Resource

from utils.data import Data
from models.users import Users


class Register(Resource):
    @staticmethod
    def post(self):
        args = request.get_json()
        args = dict()
        user = Users()
        user.username = args['username']
