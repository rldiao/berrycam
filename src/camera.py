import os
from picamera import PiCamera
from dependency_injector import providers
from datetime import datetime
from collections import OrderedDict

from src.errors.camera import CameraClosedError, CameraSettingsError

import logging
logger = logging.getLogger(__name__)


class _PiCameraWrapper:
    """
    Private Class PiCamera Wrapper. Controls operations of PiCamera. Should be Singleton
    """
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
    resolutions = OrderedDict([
        ('CGA', (320, 200)),		('QVGA', (320, 240)),
        ('VGA', (640, 480)),		('PAL', (768, 576)),
        ('480p', (720, 480)),		('576p', (720, 576)),
        ('WVGA', (800, 480)),		('SVGA', (800, 600)),
        ('FWVGA', (854, 480)),		('WSVGA', (1024, 600)),
        ('XGA', (1024, 768)),		('HD_720', (1280, 720)),
        ('WXGA_1', (1280, 768)),	('WXGA_2', (1280, 800)),
        ('SXGA', (1280, 1024)),		('SXGA+', (1400, 1050)),
        ('UXGA', (1600, 1200)),		('WSXGA+', (1680, 1050)),
        ('HD_1080', (1920, 1080)), 	('WUXGA', (1920, 1200)),
        ('2K', (2048, 1080)),		('QXGA', (2048, 1536)),
        ('QHD', (2560, 1440)),      ('WQXGA', (2560, 1600)),
        ('4k', (3840, 2160)),       ('MAX', (4056, 3040)),
    ])
    AWB_MODES = [
        'off',
        'auto',
        'sunlight',
        'cloudy',
        'shade',
        'tungsten',
        'fluorescent',
        'incandescent',
        'flash',
        'horizon'
    ]

    def __init__(self, camera: PiCamera, save_directory=None):
        if camera.closed:
            raise CameraClosedError(
                "Trying to initialise _PiCameraWrapper with closed camera")
        self.__camera = camera
        # Files
        self.save_directory = save_directory
        # Image
        self.image_format = self.image_formats[0]
        # self.resolution = self.resolutions['MAX']
        self.awb_mode = 'off'

    @property
    def closed(self):
        """Returns if camera is closed"""
        return self.__camera.closed

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

    @property
    def resolution(self):
        """Returns resolution setting value"""
        return self._resolution

    @resolution.setter
    def resolution(self, mode):
        """Sets resolution setting value"""
        if mode not in self.resolutions.keys():
            # Create custom Resolution exception
            raise Exception()
        self._resolution = self.resolutions[mode]

    @property
    def awb_mode(self):
        """Returns auto white balance mode"""
        return self._awb_mode

    @awb_mode.setter
    def awb_mode(self, awb_mode):
        """Sets auto white balance mode"""
        logger.debug('Set camera awb mode - {}'.format(awb_mode))
        if awb_mode not in self.__camera.AWB_MODES:
            raise CameraSettingsError(
                'Auto white balance mode {} not supported'.format(awb_mode))
        self._awb_mode = awb_mode
        self.__camera.awb_mode = self._awb_mode

    def preview_on(self):
        """Turns on camera preview"""
        logger.info('Camera Preview - ON')
        self.__camera.preview_fullscreen = False
        self.__camera.preview_window = (90, 100, 320, 240)
        self.__camera.resolution = (640, 480)
        self.__camera.start_preview()

    def preview_off(self):
        """Turns off camera preview"""
        logger.info('Camera Preview - OFF')
        self.__camera.stop_preview()

    def capture(self):
        """Capture image"""
        # TODO: Customisable naming
        output = '{path}/{filename}.{format}'.format(path=self.save_directory,
                                                     filename=datetime.now(),
                                                     format=self.image_format)
        logger.info('Capturing photo and saving to {}'.format(output))
        self.__camera.capture(output, format=self.image_format)


camera_provider = providers.Singleton(_PiCameraWrapper)


if __name__ == "__main__":
    with PiCamera() as pc:
        c = camera_provider(pc)
        print(c.resolution)

# TODO: Turn this into unit test
# # Retrieving several UserService objects:
# camera_handler_provider1 = camera_handler_provider()
# camera_handler_provider2 = camera_handler_provider()


# # Making some asserts:
# assert camera_handler_provider1 is camera_handler_provider2
