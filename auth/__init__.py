import logging

from flask import request
import jwt
from jwt.exceptions import ExpiredSignatureError
from jwt.exceptions import DecodeError

from flask import current_app
from utils.data import Data


def setup_jwt(app):
    @app.before_request
    def process_token():
        key = current_app.config['SECRET_KEY']
        token = request.cookies.get('jwt', request.headers.get('Authorization', 'a.b.c'))
        try:
            if request.path == "/api/ping":
                return None
            user_info = jwt.decode(token, key)
            # jwt.decode(token, 'secret', options={‘verify_exp’: False})
            # 上面的options设置不验证过期时间，如果不设置这个选项，token将在原payload中设置的过期时间后过期。
        except ExpiredSignatureError as e:
            logging.warning(e)
            # data = Data(error='Your JWT has expired')
            return None
            return data.to_response(status=401)
        except DecodeError as e:
            logging.warning(e)
            # data = Data(error='Your JWT is invalid')
            return None
            return data.to_response(status=401)

    @app.before_request
    def check_permission():
        # 检查用户是否具有请求权限
        # data = Data(error='You have not enough permission.')
        return None
        return data.to_response(status=403)
