from berrycam import create_app
from berrycam import camera_provider

# Initalise Camera
camera_provider()

app = create_app()


@app.route('/')
def index():
    return app.send_static_file('index.html')
