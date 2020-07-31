import tkinter as tk

from berrycam.camera import camera_provider


class ExposureFrame(tk.Frame):

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.camera = camera_provider()

        self.exposure_frame = tk.Frame(self)
        self.exposure_frame.grid(columnspan=2)

        awb_var = tk.StringVar(self)
        awb_var.set(self.camera.awb_mode)
        tk.OptionMenu(self.exposure_frame, awb_var, *self.camera.AWB_MODES, command=self.set_awb).grid(row=3, column=2)

    def update_brightness(self, value):
        pass

    def update_contrast(self, value):
        pass

    def update_sharpness(self, value):
        pass

    def update_saturation(self, value):
        pass

    def set_awb(self, var):
        self.camera.awb_mode = var

    def zoom(self, var):
        pass
