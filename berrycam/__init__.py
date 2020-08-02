from flask import Flask

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


def create_app():
    app = Flask(__name__, static_folder='./build', static_url_path='/', instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Import application components
        from berrycam.camera.apis import camera_api_bp

        # Register blueprints
        app.register_blueprint(camera_api_bp)

    return app
