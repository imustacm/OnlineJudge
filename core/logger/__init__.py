import logging.config


class Logger(object):
    def __init__(self, app=None):
        self.app = app
        self.debug = None
        self.info = None
        self.warn = None
        self.error = None
        self.critical = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        logging.config.dictConfig(app.config['LOGGING_CONFIG'])
        log = logging.getLogger(app.config['ENV'])
        self.debug = log.debug
        self.info = log.info
        self.warn = log.warning
        self.error = log.error
        self.critical = log.critical


logger = Logger()


def setup_logging(app):
    logger.init_app(app)
