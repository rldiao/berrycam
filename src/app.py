from time import sleep
from picamera import PiCamera

from camera import PiCameraWrapper


class BerryCam:
    
    def __init__(self, camera: PiCamera):
        self.camera = PiCameraWrapper(camera)

    def run(self):
        print('Running BerryCam...')
        self.camera.on()
        sleep(3)
