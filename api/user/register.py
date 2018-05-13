from flask_restful import Resource
from flask import request

from models.users import Users
from utils.data import Data
from core.db import db


class Register(Resource):
    @staticmethod
    def post():
        request_data = request.get_json()
        if request_data is None:
            data = Data(message='Bad request', status=400)
            return data.to_response()
        user = Users()
        try:
            user.username = request_data['username']
            user.password = request_data['password']
            user.email = request_data['email']
        except KeyError:
            data = Data(message='Bad request', status=400)
            return data.to_response()
        db.session.add(user)
        db.session.commit()
        return Data(message='Registered', status=201).to_response()
