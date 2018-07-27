from flask import Blueprint
from flask_restful import Api
from .contest_num import CountContestNumber
from .contest_list import ContestList
from .contest_info import ContestInfo

contest_blueprint = Blueprint('contest_blueprint', __name__)
contest_api = Api(contest_blueprint, prefix="/api/contests")

contest_api.add_resource(CountContestNumber, CountContestNumber.api_url)
contest_api.add_resource(ContestList, ContestList.api_url)
contest_api.add_resource(ContestInfo, ContestInfo.api_url)
