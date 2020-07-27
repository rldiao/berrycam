from time import sleep
from picamera import PiCamera

MAX_RES = (4056, 3040)
LOW_RES = (1024, 768)

try:
    camera = PiCamera()
    camera.resolution=LOW_RES
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(
        'test.jpeg',
        format='jpeg',
        quality=100
    )
finally:
    camera.close()
