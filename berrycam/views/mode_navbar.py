import tkinter as tk

import logging

logger = logging.getLogger(__name__)


class ModeNavBar(tk.Frame):
    def __init__(self, parent, mode_view, *args, **kwargs):
        super().__init__(parent)
        self.parent = parent
        self.mode_view = mode_view
        self['padx'] = 10

        for col in range(3):
            tk.Grid.columnconfigure(self, col, weight=1)

        photo_btn = tk.Button(self, text='Photo', command=self.photo_mode, width=20)
        photo_btn.grid(row=0, column=0, columnspan=1, stick='nsew')

        video_btn = tk.Button(self, text='Video', command=self.video_mode, width=20)
        video_btn.grid(row=0, column=1, columnspan=1, stick='nsew')

        settings_btn = tk.Button(self, text='Timelapse', command=self.timelapse_mode, width=20)
        settings_btn.grid(row=0, column=2, columnspan=1, stick='nsew')

    def photo_mode(self):
        self.mode_view.photo_mode()

    def video_mode(self):
        self.mode_view.video_mode()

    def timelapse_mode(self):
        self.mode_view.timelapse_mode()
