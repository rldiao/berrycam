class CameraClosedError(Exception):
    """ Camera is unexceptedly closed """
    pass


class CameraFormatError(Exception):
    """ Unsupported camera format or file extension """
    pass
