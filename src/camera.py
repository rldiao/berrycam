import os
from picamera import PiCamera
from dependency_injector import providers
from datetime import datetime

from src.errors.camera import CameraClosedError, CameraFormatError

import logging
logger = logging.getLogger(__name__)


class _PiCameraWrapper:
    """
    Private Class PiCamera Wrapper. Controls operations of PiCamera. Should be Singleton
    """

    def __init__(self, camera: PiCamera, save_directory=None):
        if camera.closed:
            raise CameraClosedError(
                "Trying to initialise _PiCameraWrapper with closed camera")
        self.__camera = camera

        self.save_directory = save_directory
        self.image_format = 'jpeg'

    @property
    def closed(self):
        return self.__camera.closed

    @property
    def save_directory(self):
        return self._save_directory

    @save_directory.setter
    def save_directory(self, save_directory=None):
        """Set where videos and photos are saved on Pi. Default to user Desktop

        Args:
            save_directory (string): String to save directory
        """
        if save_directory is None:
            self._save_directory = os.path.join(
                os.environ['HOME'], 'Desktop', 'BerryCam')
            if not os.path.exists(self._save_directory):
                os.makedirs(self._save_directory)
        else:
            self._save_directory = save_directory

        logger.debug('Save directory - {}'.format(self._save_directory))

    @property
    def image_format(self):
        return self._image_format

    @image_format.setter
    def image_format(self, image_format):
        if image_format not in ['jpeg', 'png', 'gif', 'bmp', 'yuv', 'rgb', 'rgba', 'bgr', 'bgra']:
            raise CameraFormatError('{} not supported'.format(image_format))
        self._image_format = image_format

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
        # TODO: Customisable naming
        output = '{path}/{filename}.{format}'.format(path=self.save_directory,
                                                     filename=datetime.now(),
                                                     format=self.image_format)
        logger.info('Capturing photo and saving to {}'.format(output))
        self.__camera.capture(output, format=self.image_format)


camera_provider = providers.Singleton(_PiCameraWrapper)

# TODO: Turn this into unit test
# # Retrieving several UserService objects:
# camera_handler_provider1 = camera_handler_provider()
# camera_handler_provider2 = camera_handler_provider()


# # Making some asserts:
# assert camera_handler_provider1 is camera_handler_provider2
