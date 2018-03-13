import time

from flask import current_app
from flask_restful import Resource
from flask_restful import reqparse
import jwt

from models.users import Users
from utils.data import Data
from utils.time import DAY

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Login(Resource):
    @staticmethod
    def get():
        data = Data(data="Not allow function", status=403)
        return data.to_response()

    @staticmethod
    def post():
        exp = int(time.time()) + DAY  # 失效时间
        key = current_app.config['SECRET_KEY']
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        payload = {'exp': exp, 'user': username}  # JSON 数据
        token = jwt.encode(payload, key)
        user = Users.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            data = Data(data='Username or Password Error.', status=200)
            return data.to_response()
        data = Data(data=token.decode('utf8'), status=200).to_response()
        data.set_cookie('jwt', token)
        return data
