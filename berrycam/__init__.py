from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        # Import application components
        from berrycam.camera.apis import camera_api_bp
        from berrycam.camera.views import camera_view_bp

        # Register blueprints
        app.register_blueprint(camera_api_bp)
        app.register_blueprint(camera_view_bp)

    return app
