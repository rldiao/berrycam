from flask import Blueprint, request, jsonify

from berrycam.camera import camera_provider
from berrycam.camera.helpers import invalid_settings

camera_bp = Blueprint(
    'camera_bp',
    __name__,
    url_prefix='/camera'
)


@camera_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    # TODO: Need better type protection
    camera = camera_provider()

    if request.method == 'GET':
        return jsonify(camera.settings)

    if request.method == 'POST':
        new_settings = request.get_json()
        errors = invalid_settings(camera, new_settings)
        if invalid_settings:
            return jsonify({
                'invalid_settings': errors,
            }), 400
        return jsonify(camera.settings)


@camera_bp.route('/toggle_preview', methods=['GET'])
def toggle_preview():
    response = {}
    status_code = 200
    try:
        camera_provider().toggle_preview()
    except Exception as e:
        response['error'] = {
            'type': type(e),
            'message': str(e)
        }
        status_code = 500
    response['message'] = 'Preview Off' if camera_provider().preview is None else 'Preview On'
    return jsonify(response), status_code


@camera_bp.route('/capture', methods=['GET'])
def capture():
    response = {}
    status_code = 200
    try:
        response['filename'] = camera_provider().capture()
    except Exception as e:
        response['error'] = {
            'type': type(e),
            'message': str(e)
        }
        status_code = 500
    return jsonify(response), status_code
