"""
Auth: Yaqiong
Email: waishushu@outlook.com
Time: 11 Mar 2018 17:08
Notice:
    If anything goes wrong, please don't contact me.
    If everything is OK, please do email me with a "Thank you" message.

~~~~~~~~~~~~~~~~

flask注册蓝本, 在这里统一进行注册管理, 在项目创建app时调用

需要导入对应的对象 & 注册

"""


def setup_bluepoints(app):
    from api import blueprint_list
    for item in blueprint_list:
        app.register_blueprint(item)
