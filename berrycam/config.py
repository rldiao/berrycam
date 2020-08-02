import logging
from logging.config import dictConfig


class BaseConfig:
    SECRET_KEY = 'GDtfDCFYjD'


class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    logging_config = dict(
        version=1,
        formatters={
            'f': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        handlers={
            'stream': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.INFO
            }
        },
        root={
            'handlers': ['stream'],
            'level': logging.INFO,
        },
    )

    dictConfig(logging_config)


class DevConfig(BaseConfig):
    # This double boots app, one as debugger
    DEBUG = False
    TESTING = True

    logging_config = dict(
        version=1,
        formatters={
            'f': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        handlers={
            'stream': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.DEBUG
            }
        },
        root={
            'handlers': ['stream'],
            'level': logging.DEBUG,
        },
    )

    dictConfig(logging_config)
