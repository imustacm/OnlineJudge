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
    from api import user_blueprint
    app.register_blueprint(user_blueprint)
    from api import problem_blueprint
    app.register_blueprint(problem_blueprint)
    from api import ping_blueprint
    app.register_blueprint(ping_blueprint)
    from api import captcha_blueprint
    app.register_blueprint(captcha_blueprint)
    from api import contest_blueprint
    app.register_blueprint(contest_blueprint)
    from api import submission_blueprint
    app.register_blueprint(submission_blueprint)
    from api import rank_blueprint
    app.register_blueprint(rank_blueprint)
