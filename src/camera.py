from picamera import PiCamera
from dependency_injector import providers

from src.errors.camera import CameraClosedError


class PiCameraWrapper:
    """
    Singleton PiCamera Wrapper 
    """

    def __init__(self, camera: PiCamera):
        if camera.closed:
            raise CameraClosedError("Trying to initialise PiCameraWrapper with closed camera")
        self.camera = camera

    def on(self):
        print('Turning on camera...')
        self.camera.preview_fullscreen = False
        self.camera.preview_window = (90, 100, 320, 240)
        self.camera.resolution = (640, 480)
        self.camera.start_preview()

    def off(self):
        print('Turning off camera...')
        self.camera.stop_preview()


camera_provider = providers.Singleton(PiCameraWrapper)

# TODO: Turn this into unit test
# # Retrieving several UserService objects:
# camera_handler_provider1 = camera_handler_provider()
# camera_handler_provider2 = camera_handler_provider()


# # Making some asserts:
# assert camera_handler_provider1 is camera_handler_provider2
