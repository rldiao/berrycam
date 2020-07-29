import tkinter as tk

from .exposure import ExposureFrame
from .photo import PhotoFrame


class Index(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.master.geometry("320x300")
        self.master.title("BerryCam")

        preview = PhotoFrame(master=self)
        preview.pack()

        exposure = ExposureFrame(master=self)
        exposure.pack()



