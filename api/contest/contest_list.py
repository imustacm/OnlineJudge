# -*- utf-8 -*-
import time

from flask import request
from werkzeug.exceptions import BadRequestKeyError
from flask_restful import Resource

from models.contest import Contest
from utils.data import Data


class ContestList(Resource):
    public_api = True
    api_url = '/contest_list'

    @staticmethod
    def get():
        try:
            limit = int(request.args['limit'])
        except BadRequestKeyError:
            limit = 100
        except ValueError:
            data = Data(message='Invalid value of limit', status=422)
            return data.to_response()
        try:
            offset = int(request.args['offset'])
        except BadRequestKeyError:
            offset = 0
        except ValueError:
            data = Data(message='Invalid value of offset', status=422)
            return data.to_response()
        results = Contest.query.order_by(Contest.id).filter_by(visible=True).limit(limit).offset(offset).all()
        contest_list = []
        for item in results:
            contest = {
                "id": item.id,
                "title": item.title,
                "start_time": item.start_time,
                "end_time": item.end_time,
                "type": item.permission_type
            }
            now = int(time.time())
            if contest['end_time'] is None or now > contest['end_time']:
                contest['status'] = 'end'
            else:
                contest['status'] = 'running'
            contest_list.append(contest)
        data = Data(data=contest_list, status=200)
        return data.to_response()
