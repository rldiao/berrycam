import tkinter as tk

from berrycam.views.index import Index
from berrycam.camera import camera_provider

import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Running BerryCam...')
    with camera_provider():
        root_window = tk.Tk()
        root_window.resizable(height=None, width=None)
        index = Index(master=root_window)
        index.mainloop()

    logger.debug('Camera closed - {}'.format(camera_provider().closed))
