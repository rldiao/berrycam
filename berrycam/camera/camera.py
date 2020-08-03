import os
import io
from dependency_injector import providers
from datetime import datetime
from time import sleep

from berrycam.camera.errors import CameraSettingsError

try:
    from picamera import PiCamera
except ImportError:
    from fake_rpi.picamera import PiCamera

import logging

logger = logging.getLogger(__name__)


class BerryCamera(PiCamera):
    """Should be initialized via camera_provider"""
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
        # TODO: Override these properties
        # https://stackoverflow.com/questions/36336960/override-an-attribute-with-a-property-in-python-class
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

    @property
    def settings(self):
        """Returns all camera parameter"""
        settings = vars(self)
        # Remove _ from @property values
        for key in settings.keys():
            if key.startswith('_'):
                settings[key[1:]] = settings.pop(key)
        return settings

    def toggle_preview(self):
        """Toggle camera preview"""
        if self.preview is None:
            logger.info('Camera Preview - ON')
            super().start_preview()
        else:
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
        return output

    def get_frame(self):
        # let camera warm up
        sleep(2)

        stream = io.BytesIO()
        for _ in super().capture_continuous(stream, 'jpeg', use_video_port=True):
            # return current frame
            stream.seek(0)
            yield stream.read()

            # reset stream for next frame
            stream.seek(0)
            stream.truncate()


camera_provider = providers.Singleton(BerryCamera)
