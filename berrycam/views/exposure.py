import tkinter as tk

from berrycam.camera import camera_provider


class ExposureView:

    def __init__(self, parent=None, *args, **kwargs):
        self.parent = parent
        self.camera = camera_provider()

        self.frame = tk.LabelFrame(self.parent, text='Exposure')
        self.frame.grid(columnspan=2)

        awb_var = tk.StringVar(self.frame)
        awb_var.set(self.camera.awb_mode)
        tk.OptionMenu(self.frame, awb_var, *self.camera.AWB_MODES, command=self.set_awb).grid(row=3, column=2)

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
