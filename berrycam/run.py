from flask import Flask
from berrycam.camera import camera_provider

import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)

if __name__ == '__main__':
    logger.info('Running BerryCam...')
    with camera_provider():
        app.run(host='localhost', port=8000, debug=True)

    logger.debug('Camera closed - {}'.format(camera_provider().closed))
