import string
import random

from flask import url_for
from captcha.image import ImageCaptcha
from flask_restful import Resource

from core.sentinel import sentinel
from utils.time import MINUTE
from utils.key_to_hash import get_key_to_hash
from utils.data import Data


class Captcha(Resource):
    img = ImageCaptcha()
    image = img.generate_image('python')

    @staticmethod
    def generate_code(number):
        code = ''.join(random.sample(string.digits + string.ascii_letters, number))
        index = ''.join(random.sample(string.ascii_letters, 20))
        img = ImageCaptcha(fonts=['static/font/font.ttf', 'static/font/font2.ttf'])
        image = img.generate_image(code)
        filename = index + '.jpg'
        image.save('static/captcha/' + filename)
        sentinel.master.setex(get_key_to_hash('captcha', key=index), MINUTE * 5, code)
        return {'index': index, 'url': url_for('static/captcha/' + filename, _external=True)}

    @staticmethod
    def judge_code(user_code, index):
        code = sentinel.slave.get(get_key_to_hash('captcha', key=index))
        if user_code == code:
            return True
        else:
            return False

    @staticmethod
    def get():
        captcha = Captcha.generate_code(4)
        data = Data(data=captcha, status=200)
        return data.to_response()
