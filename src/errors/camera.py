class CameraClosedError(Exception):
    """Camera is unexceptedly closed"""
    pass


class CameraSettingsError(Exception):
    """Unsupported camera setting"""
    pass
