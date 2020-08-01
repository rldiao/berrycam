import tkinter as tk

from berrycam.views.photo_view.photo import PhotoView


class ModeView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.parent = parent

        self.frame = tk.Frame(self, padx='20', pady='20')
        self.frame.grid(row=0, column=0, sticky='nsew')

        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        PhotoView(self.frame)

    def photo_mode(self):
        pass

    def video_mode(self):
        pass

    def timelapse_mode(self):
        pass
