from flask import Blueprint, request, jsonify

from berrycam.camera import camera_provider

camera_bp = Blueprint(
    'camera_bp',
    __name__,
    url_prefix='/camera'
)


@camera_bp.route('/', methods=['GET', 'POST'])
def camera():
    if request.method == 'GET':
        return jsonify(camera_provider().settings)
    # elif request.method == 'POST':
    #     try:
    #         camera.image_format = str(request.data)
    #     except CameraSettingsError as e:
    #         return str(e)
    #     return camera.image_format


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
    return jsonify(response),
