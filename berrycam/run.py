from berrycam import create_app
from berrycam.camera import camera_provider

app = create_app()


@app.route('/')
def index():
    return app.send_static_file('index.html')


app.logger.info('Running BerryCam...')
camera_provider()
app.logger.debug('Camera Status - {}'.format(not camera_provider().closed))
camera_provider().close()
app.logger.debug('Camera Status - {}'.format(not camera_provider().closed))
