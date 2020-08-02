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
        return jsonify(camera_provider().__dict__)
    # elif request.method == 'POST':
    #     try:
    #         camera.image_format = str(request.data)
    #     except CameraSettingsError as e:
    #         return str(e)
    #     return camera.image_format


@camera_bp.route('/capture', methods=['GET'])
def capture():
    filename = camera_provider().capture()
    return jsonify({
        'filename': filename
    })
