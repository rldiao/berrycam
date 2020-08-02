from flask import Flask

from berrycam import create_app
from berrycam.camera import camera_provider

app = create_app()

if __name__ == '__main__':
    app.logger.info('Running BerryCam...')
    with camera_provider() as c:
        app.run(host='localhost', port=8000)
    app.logger.debug('Camera closed - {}'.format(camera_provider().closed))
