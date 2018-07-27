from flask import request
from flask_restful import Resource
from utils.data import Data
from core import celery


class C(Resource):
    url = '/task'

    @staticmethod
    def get():
        import datetime
        start = datetime.datetime.now()
        task = longtime.delay()
        end = datetime.datetime.now()
        data = Data(message="It's OK, you get me", data=task.id, status=200)
        return data.to_response()

    @staticmethod
    def post():
        request_data = request.get_json()
        data = Data(message="It's OK, you post me", data=request_data, status=200)
        return data.to_response()


class B(Resource):
    url = '/get'

    @staticmethod
    def get():
        task_id = request.args.get(key='id', type=str)
        task = longtime.AsyncResult(task_id)
        data = Data(message="It's OK, you get me", data=[task.status, task.result], status=200)
        return data.to_response()


@celery.task
def longtime():
    import time
    time.sleep(20)
    return {"hello": "fff2"}
