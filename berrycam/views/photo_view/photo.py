import tkinter as tk

from berrycam.views.photo_view.exposure import ExposureView


class PhotoView:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.frame = tk.Frame(self.parent)
        self.frame.grid(row=0, column=0)

        ExposureView(self.frame).grid()
