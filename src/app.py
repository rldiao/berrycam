from time import sleep
import tkinter as tk

try:
    from picamera import PiCamera
except ModuleNotFoundError as e:
    print(e)

from src.camera import PiCameraWrapper
from src.views.index import Index


class BerryCam:
    
    def __init__(self, camera):
        # self.camera = PiCameraWrapper(camera)
        pass

    def run(self):
        print('Running BerryCam...')
        root_window = tk.Tk()
        index = Index(master=root_window)
        index.mainloop()


if __name__ == '__main__':
    app = BerryCam(None)
    app.run()