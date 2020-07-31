import tkinter as tk

from berrycam.views.exposure import ExposureView


class ModeView:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.frame = tk.Frame(self.parent)
        self.frame.grid(row=0, column=0)

        ExposureView(self.frame)
