from picamera import PiCamera
from dependency_injector import providers
from datetime import datetime

from src.errors.camera import CameraClosedError

import logging
logger = logging.getLogger(__name__)


class PiCameraWrapper:
    """
    Singleton PiCamera Wrapper 
    """

    def __init__(self, camera: PiCamera):
        if camera.closed:
            raise CameraClosedError("Trying to initialise PiCameraWrapper with closed camera")
        self.__camera = camera

        self.photo_dir = '/home/pi/projects/berrycam/photos'

    def preview_on(self):
        logger.info('Camera Preview - ON')
        self.__camera.preview_fullscreen = False
        self.__camera.preview_window = (90, 100, 320, 240)
        self.__camera.resolution = (640, 480)
        self.__camera.start_preview()

    def preview_off(self):
        logger.info('Camera Preview - OFF')
        self.__camera.stop_preview()

    def capture(self):
        # TODO: Set extension, photo_dir, naming
        filename = '{path}/{filename}.jpeg'.format(path=self.photo_dir, filename=datetime.now())
        logger.info('Capturing photo - ')
        self.__camera.capture(filename)


camera_provider = providers.Singleton(PiCameraWrapper)

# TODO: Turn this into unit test
# # Retrieving several UserService objects:
# camera_handler_provider1 = camera_handler_provider()
# camera_handler_provider2 = camera_handler_provider()


# # Making some asserts:
# assert camera_handler_provider1 is camera_handler_provider2
