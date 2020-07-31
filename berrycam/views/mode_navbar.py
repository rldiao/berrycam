import tkinter as tk

import logging

logger = logging.getLogger(__name__)


class ModeNavBar:
    def __init__(self, parent, mode_view, *args, **kwargs):
        self.parent = parent
        self.mode_view = mode_view

        self.frame = tk.Frame(self.parent)
        self.frame.grid(stick='sew')

        for col in range(3):
            tk.Grid.columnconfigure(self.frame, col, weight=1)

        photo_btn = tk.Button(self.frame, text='Photo', command=self.photo_mode)
        photo_btn.grid(row=0, column=0, stick='nsew')

        video_btn = tk.Button(self.frame, text='Video', command=self.video_mode)
        video_btn.grid(row=0, column=1, stick='nsew')

        setting_btn = tk.Button(self.frame, text='Setting', command=self.setting_mode)
        setting_btn.grid(row=0, column=2, stick='nsew')

    def photo_mode(self):
        logger.info('photo mode')
        self.mode_view.frame.configure(bg='red')

    def video_mode(self):
        logger.info('video mode')
        self.mode_view.frame.configure(bg='green')

    def setting_mode(self):
        logger.info('setting mode')
        self.mode_view.frame.configure(bg='blue')
