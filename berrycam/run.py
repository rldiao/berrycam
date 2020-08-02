from flask import Flask

from berrycam import create_app
from berrycam.camera import camera_provider

app = create_app()

app.logger.info('Running BerryCam...')
camera_provider()
app.logger.debug('Camera Status - {}'.format(not camera_provider().closed))
camera_provider().close()
app.logger.debug('Camera Status - {}'.format(not camera_provider().closed))
