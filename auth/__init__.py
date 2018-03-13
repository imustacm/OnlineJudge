try:
    import cPickle as pickle
except ImportError:  # pragma: no cover
    import pickle

from flask import request
import logging
import jwt
from jwt.exceptions import ExpiredSignatureError
from jwt.exceptions import DecodeError

from flask import current_app
from utils.data import Data
from core.sentinel import sentinel

from functools import wraps


def login_require(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'login_require', True):
            return func(*args, **kwargs)
        token = request.cookies.get('jwt', request.headers.get('Authorization', 'a.b.c'))
        secret_key = current_app.config['SECRET_KEY']
        try:
            user_info = jwt.decode(token, secret_key)
            username = user_info['user']
            real_token = pickle.loads(sentinel.slave.get('login:%s' % username)).decode()
            if real_token != token:
                data = Data(data='Your JWT is invalid', status=401)
                return data.to_response()
        except ExpiredSignatureError as e:
            logging.warning(e)
            data = Data(data='Your JWT has expired', status=401)
            return data.to_response()
        except DecodeError as e:
            logging.warning(e)
            data = Data(data='Your JWT is invalid', status=401)
            return data.to_response()
        return func(*args, **kwargs)

    return wrapper
