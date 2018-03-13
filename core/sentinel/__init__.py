from redis import sentinel as se
from redis import StrictRedis


class Sentinel(object):
    def __init__(self, app=None):
        self.app = app
        self.connection = None
        self.master = StrictRedis()
        self.slave = self.master
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.connection = se.Sentinel(app.config['REDIS_SENTINEL'], socket_timeout=0.1)
        redis_db = app.config.get('REDIS_DB') or 0
        self.master = self.connection.master_for('mymaster', db=redis_db)
        self.slave = self.connection.slave_for('mymaster', db=redis_db)


sentinel = Sentinel()


def setup_sentinel(app):
    sentinel.init_app(app)
