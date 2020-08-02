from flask import Flask, current_app

import berrycam.config


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Import application components
        from berrycam.camera.controller import camera_bp

        # Register blueprints
        app.register_blueprint(camera_bp)

    return app
