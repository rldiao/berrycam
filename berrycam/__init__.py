import atexit
from flask import Flask
from berrycam.camera import camera_provider

import logging
from logging.config import dictConfig


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


def clean_exit(logger, *args, **kwargs):
    camera_provider().close()
    print('')
    logger.info('Camera Status - {}'.format(not camera_provider().closed))


def create_app():
    app = Flask(__name__, static_folder='./build', static_url_path='/', instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    app.logger.info('Running BerryCam')
    camera = camera_provider()
    app.logger.info('Camera Status - {}'.format(not camera.closed))

    with app.app_context():
        # Import application components
        from berrycam.camera.apis import camera_api_bp

        # Register blueprints
        app.register_blueprint(camera_api_bp)

    atexit.register(clean_exit, app.logger)

    return app
