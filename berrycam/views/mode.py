import tkinter as tk

from berrycam.views.photo_view.photo import PhotoView


class ModeView:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.frame = tk.Frame(self.parent, padx='20', pady='20')
        self.frame.grid(row=0, column=0, sticky='nsew')

        tk.Grid.rowconfigure(self.parent, 0, weight=1)
        tk.Grid.columnconfigure(self.parent, 0, weight=1)

        PhotoView(self.frame)

    def photo_mode(self):
        pass

    def video_mode(self):
        pass

    def timelapse_mode(self):
        pass
