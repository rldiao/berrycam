from picamera import PiCamera


class PiCameraWrapper:
    camera = None

    def __init__(self, camera: PiCamera):
        if PiCameraWrapper.camera is None:
            PiCameraWrapper.camera = camera

    def on(self):
        print('Turning on camera...')
        self.camera.preview_fullscreen = False
        self.camera.preview_window = (90, 100, 320, 240)
        self.camera.resolution = (640, 480)
        self.camera.start_preview()

    def off(self):
        print('Turning off camera...')
        self.camera.stop_preview()
