from datetime import datetime
from flask_restful import Resource
from flask import request
from werkzeug.exceptions import BadRequestKeyError

from models.contest import Contest
from utils.data import Data


class ContestInfo(Resource):
    api_url = '/contest_info'

    @staticmethod
    def get():
        try:
            contest_id = int(request.args['id'])
        except (BadRequestKeyError, ValueError):
            data = Data(message='Invalid value of contest_id', status=422)
            return data.to_response()
        result = Contest.query.filter_by(id=contest_id, visible=True).first()
        if result is None:
            return Data(data=[], status=404, message='not found message about `%s`' % contest_id).to_response()
        contest = dict()
        contest['id'] = result.id
        contest['start_time'] = result.start_time
        contest['end_time'] = result.end_time
        now = datetime.now()
        if contest['end_time'] < now:
            contest['status'] = 'end'
        elif contest['start_time'] < now < contest['end_time']:
            contest['status'] = 'running'
        else:
            contest['status'] = 'pending'
        data = Data(data=contest, status=200)
        return data.to_response()
