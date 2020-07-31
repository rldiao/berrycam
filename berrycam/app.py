import tkinter as tk

from berrycam.views.index import Index
from berrycam.camera import camera_provider

import logging

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('Running BerryCam...')
    with camera_provider():
        root_window = tk.Tk()
        index = Index(root_window)
        root_window.mainloop()

    logger.debug('Camera closed - {}'.format(camera_provider().closed))
