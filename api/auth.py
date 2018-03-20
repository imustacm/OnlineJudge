import time
from core.logger import logger

from core.db import db
from models import LoginLog
from sqlalchemy import exc
from flask import current_app, request
from flask_restful import Resource
from flask_restful import reqparse

import jwt

try:
    import cPickle as pickle
except ImportError:  # pragma: no cover
    import pickle

from models.users import Users
from utils.key_to_hash import get_key_to_hash
from utils.data import Data
from utils.time import DAY

from core.sentinel import sentinel

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
        secret_key = current_app.config['SECRET_KEY']
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        payload = {'exp': exp, 'user': username}  # JSON 数据
        token = jwt.encode(payload, secret_key)
        user = Users.query.filter_by(username=username).first()

        login_log = LoginLog()
        login_log.user_id = username
        login_log.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        login_log.ip = request.remote_addr

        flag = 0
        if not user or not user.verify_password(password):
            data = Data(data='Username or Password Error.', status=200)
            login_log.success_flag = False
        else:
            flag = 1
            login_log.success_flag = True
            key = get_key_to_hash('login', username=username)
            sentinel.master.setex(key, DAY, pickle.dumps(token))
            data = Data(data=token.decode('utf8'), status=200).to_response()
            data.set_cookie('jwt', token)

        try:
            db.session.add(login_log)
            db.session.commit()
        except exc.IntegrityError as e:
            logger.warn(e)
            db.session.rollback()
            db.session.close()
            
        if flag == 0:
            return data.to_response()
        else:
            return data
