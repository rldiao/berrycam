import os
from picamera import PiCamera
from dependency_injector import providers
from datetime import datetime
# from collections import OrderedDict

from src.errors.camera import CameraSettingsError

import logging
logger = logging.getLogger(__name__)


class BerryCamera(PiCamera):
    image_formats = [
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
    # RESOLUTION_MODES = OrderedDict([
    #     ('CGA', (320, 200)),		('QVGA', (320, 240)),
    #     ('VGA', (640, 480)),		('PAL', (768, 576)),
    #     ('480p', (720, 480)),		('576p', (720, 576)),
    #     ('WVGA', (800, 480)),		('SVGA', (800, 600)),
    #     ('FWVGA', (854, 480)),		('WSVGA', (1024, 600)),
    #     ('XGA', (1024, 768)),		('HD_720', (1280, 720)),
    #     ('WXGA_1', (1280, 768)),	('WXGA_2', (1280, 800)),
    #     ('SXGA', (1280, 1024)),		('SXGA+', (1400, 1050)),
    #     ('UXGA', (1600, 1200)),		('WSXGA+', (1680, 1050)),
    #     ('HD_1080', (1920, 1080)), 	('WUXGA', (1920, 1200)),
    #     ('2K', (2048, 1080)),		('QXGA', (2048, 1536)),
    #     ('QHD', (2560, 1440)),      ('WQXGA', (2560, 1600)),
    #     ('4k', (3840, 2160)),       ('MAX', (4056, 3040)),
    # ])

    def __init__(self, save_directory=None):
        super(BerryCamera, self).__init__()
        # Files
        self.save_directory = save_directory
        # Preview
        self.preview_fullscreen = False
        self.preview_window = (90, 100, 320, 240)
        # Image
        self.image_format = self.image_formats[0]

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
        """Sets image format based on self.image_formats"""
        if image_format not in self.image_formats:
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

# TODO REMOVE
if __name__ == "__main__":
    with camera_provider() as c:
        print('hello')

# TODO: Turn this into unit test
# # Retrieving several UserService objects:
# camera_handler_provider1 = camera_handler_provider()
# camera_handler_provider2 = camera_handler_provider()


# # Making some asserts:
# assert camera_handler_provider1 is camera_handler_provider2
