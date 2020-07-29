import tkinter as tk
from picamera import PiCamera

from src.views.index import Index
from src.camera import camera_provider

import logging
logger = logging.getLogger(__name__)


class BerryCam:
    def run(self):
        logger.info('Running BerryCam...')
        with PiCamera() as pc:
            camera_provider(pc)
            root_window = tk.Tk()
            index = Index(master=root_window)
            index.mainloop()


if __name__ == '__main__':
    app = BerryCam()
    app.run()
