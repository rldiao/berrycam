from berrycam.camera.camera import BerryCamera


def invalid_settings(camera: BerryCamera, settings: dict):
    """Checks if all settings in new settings are settings in camera

    Returns:
        list of settings that cannot be set in camera
    """
    invalid_settings = []
    for setting in settings.keys():
        if setting not in camera.settings.keys():
            invalid_settings.append(setting)
    return invalid_settings
