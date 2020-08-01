import os
from dependency_injector import providers
from datetime import datetime

from berrycam.errors.camera import CameraSettingsError

try:
    from picamera import PiCamera
except ImportError:
    from fake_rpi.picamera import PiCamera

import logging

logger = logging.getLogger(__name__)


class BerryCamera(PiCamera):
    IMAGE_FORMATS = [
        'jpeg',
        'png',
        'gif',
        'bmp',
        'yuv',
        'rgb',
        'rgba',
        'bgr',
        'bgra'
    ]

    def __init__(self, save_directory=None):
        super(BerryCamera, self).__init__()
        # Files
        self.save_directory = save_directory
        # Preview
        self.preview_fullscreen = False
        self.preview_window = (90, 100, 320, 240)
        # Image
        self.image_format = self.IMAGE_FORMATS[0]

    def __repr__(self):
        # TODO: Improve this
        return str(self.__dict__)

    @property
    def save_directory(self):
        """Returns file save directory"""
        return self._save_directory

    @save_directory.setter
    def save_directory(self, save_directory=None):
        """Set where files are saved on Pi. Default to user Desktop"""
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
        """Returns image format setting value"""
        return self._image_format

    @image_format.setter
    def image_format(self, image_format):
        """Sets image format based on self.IMAGE_FORMATS"""
        if image_format not in self.IMAGE_FORMATS:
            raise CameraSettingsError(
                'Image format {} not supported'.format(image_format))
        self._image_format = image_format

    def start_preview(self):
        """Turns on camera preview"""
        logger.info('Camera Preview - ON')
        super().start_preview()

    def stop_preview(self):
        """Turns off camera preview"""
        logger.info('Camera Preview - OFF')
        super().stop_preview()

    def capture(self):
        """Capture image"""
        # TODO: Customisable naming
        output = '{path}/{filename}.{format}'.format(path=self.save_directory,
                                                     filename=datetime.now(),
                                                     format=self.image_format)
        logger.info('Capturing photo and saving to {}'.format(output))
        logger.debug('Camera Settings - {}'.format(repr(self)))
        super().capture(output, format=self.image_format)


camera_provider = providers.Singleton(BerryCamera)
