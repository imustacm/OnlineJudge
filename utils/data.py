"""

utils.data

Auth: Yaqiong
Email: waishushu@outlook.com
Time: 11 Mar 2018 17:13
Notice:
    If anything goes wrong, please don't contact me.
    If everything is OK, please do email me with a "Thank you" message.

~~~~~~~~~~~~~~~~

一个简单的类去生成一个response并返回。

假设你需要返回的response是json。并且使用下面的格式：

{
    "status" : ... ,
    "data": ... ,
    "message" : ...
}
你可以尝试使用该类

usage:
    data = Data(status=200, data=your_data, message=your_message)
    return data.to_response()

notice:
    1. status, data的数据必须选定, 如果data为空,传入空list对象即可
    2. message是可选择的。在你需要有一些错误提示或者其他可以使用
    3. 并不会检查你传入的数据是否合法, 是否可以解析为json格式
    4. status 会作为HTTP状态码并且返回给浏览器, 最好遵循http标准
    5. 我并不知道下面的代码有没有什么奇怪的BUG, 如果出现了问题, 请别联系我

"""
from flask import jsonify
from flask import make_response


class Data(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'data' not in kwargs:
            raise DataException('Data must be given.')
        if 'status' not in kwargs:
            raise DataException('Status must be given.')
        self['status'] = kwargs['status']
        self['data'] = kwargs['data']
        if 'message' in kwargs:
            self['message'] = kwargs['message']

    def to_response(self):
        status = self['status']
        return make_response(jsonify(self), status)


class DataException(Exception):
    pass


if __name__ == "__main__":
    data = Data()
    print(data)
