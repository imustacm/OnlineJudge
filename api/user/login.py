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
from models.users import Users
from utils.key_to_hash import get_key_to_hash
from utils.data import Data
from utils.time import DAY

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Login(Resource):
    @staticmethod
    def post():
        exp = int(time.time()) + DAY  # 失效时间
        secret_key = current_app.config['SECRET_KEY']
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        if not username or not password:
            return Data(message='Username or Password Error.', status=200).to_response()
        payload = {'exp': exp, 'user': username}  # JSON 数据

        token = jwt.encode(payload, secret_key)
        user = Users.query.filter_by(username=username).first()

        login_log = LoginLog()
        login_log.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        login_log.ip = request.remote_addr
        if user is not None:
            login_log.user_id = user.id
        else:
            login_log.user_id = 0
        if not user or not user.verify_password(password):
            data = Data(message='Username or Password Error.', status=200).to_response()
            login_log.success_flag = False
        else:
            login_log.success_flag = True
            key = get_key_to_hash('login', username=username)
            sentinel.master.setex(key, DAY, pickle.dumps(token))
            data = Data(data=token.decode('utf8'), status=200).to_response()
            data.set_cookie('jwt', token)

        try:
            db.session.add(login_log)
            db.session.commit()
        except IntegrityError as e:
            logger.warn(e)
            db.session.rollback()
            db.session.close()

        return data
