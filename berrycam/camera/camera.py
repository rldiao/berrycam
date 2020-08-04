import os
import io
import inspect
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
        return str({**self.__dict__, **super().__dict__})

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
        return {
            'analog_gain': str(self.analog_gain),
            'annotate_background': str(self.annotate_background),
            'annotate_foreground': str(self.annotate_foreground),
            'annotate_frame_num': str(self.annotate_frame_num),
            'annotate_text': str(self.annotate_text),
            'annotate_text_size': str(self.annotate_text_size),
            'awb_gains': str(self.awb_gains),
            'awb_mode': str(self.awb_mode),
            'brightness': str(self.brightness),
            'clock_mode': str(self.clock_mode),
            'closed': str(self.closed),
            'color_effects': str(self.color_effects),
            'contrast': str(self.contrast),
            'crop': str(self.crop),
            'digital_gain': str(self.digital_gain),
            'drc_strength': str(self.drc_strength),
            'exif_tags': str(self.exif_tags),
            'exposure_compensation': str(self.exposure_compensation),
            'exposure_mode': str(self.exposure_mode),
            'exposure_speed': str(self.exposure_speed),
            'flash_mode': str(self.flash_mode),
            'framerate': str(self.framerate),
            'framerate_delta': str(self.framerate_delta),
            'framerate_range': str(self.framerate_range),
            'hflip': str(self.hflip),
            'image_denoise': str(self.image_denoise),
            'image_effect': str(self.image_effect),
            'image_effect_params': str(self.image_effect_params),
            'image_format': str(self.image_format),
            'iso': str(self.iso),
            'meter_mode': str(self.meter_mode),
            'overlays': str(self.overlays),
            'preview': str(self.preview),
            'preview_alpha': str(self.preview_alpha),
            'preview_fullscreen': str(self.preview_fullscreen),
            'preview_layer': str(self.preview_layer),
            'preview_window': str(self.preview_window),
            'previewing': str(self.previewing),
            'raw_format': str(self.raw_format),
            'recording': str(self.recording),
            'resolution': str(self.resolution),
            'revision': str(self.revision),
            'rotation': str(self.rotation),
            'saturation': str(self.saturation),
            'save_directory': str(self.save_directory),
            'sensor_mode': str(self.sensor_mode),
            'sharpness': str(self.sharpness),
            'shutter_speed': str(self.shutter_speed),
            'still_stats': str(self.still_stats),
            'vflip': str(self.vflip),
            'video_denoise': str(self.video_denoise),
            'video_stabilization': str(self.video_stabilization),
            'zoom': str(self.zoom),
        }

    def toggle_preview(self):
        """Toggle camera preview"""
        if self.preview is None:
            logger.info('Camera Preview - ON')
            super().start_preview()
        else:
            logger.info('Camera Preview - OFF')
            super().stop_preview()

    @property
    def filename_format(self):
        """Filenaming format string following python .format syntax"""
        return self._filename_format

    @filename_format.setter
    def filename_format(self, filename_format: str):
        self._filename_format = filename_format

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

        stream.close()
        logger.info('Stream closed')


camera_provider = providers.Singleton(BerryCamera)


if __name__ == "__main__":
    camera = BerryCamera()
    for attr, _ in inspect.getmembers(BerryCamera, predicate=lambda obj: isinstance(obj, property)):
        if attr not in ['frame', 'led', 'settings']:
            print("'{}': str(self.{}),".format(attr, attr))
