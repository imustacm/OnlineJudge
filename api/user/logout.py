import time
from core.logger import logger

from core.db import db
from models import LoginLog
from sqlalchemy.exc import IntegrityError
from flask import current_app, request
from flask_restful import Resource
from flask_restful import reqparse
import jwt
from jwt.exceptions import ExpiredSignatureError
from jwt.exceptions import DecodeError

try:
    import cPickle as pickle
except ImportError:  # pragma: no cover
    import pickle

from core.sentinel import sentinel
from auth import login_require
from utils.data import Data
from utils.key_to_hash import get_key_to_hash

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Logout(Resource):
    method_decorators = [login_require]

    @staticmethod
    def post():
        token = request.cookies.get('jwt', request.headers.get('Authorization', 'a.b.c'))
        secret_key = current_app.config['SECRET_KEY']
        user_info = jwt.decode(token, secret_key)
        username = user_info['user']
        key = get_key_to_hash('login', username=username)
        data = Data(message='logout success', status=200).to_response()
        data.delete_cookie('jwt')
        sentinel.master.delete(key)
        return data
