from flask import Blueprint, request, jsonify, render_template

camera_view_bp = Blueprint(
    'camera_view_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/camera'
)


@camera_view_bp.route('/')
def index():
    return render_template('index.html')
