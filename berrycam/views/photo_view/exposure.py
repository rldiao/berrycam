import tkinter as tk

from berrycam.camera import camera_provider


class ExposureView(tk.LabelFrame):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.parent = parent
        self.camera = camera_provider()
        
        self['text'] = 'Exposure'

        # TODO: Move these to new subsections of photo mode
        tk.Scale(self, from_=30, to=100, orient=tk.HORIZONTAL, label="Brightness").grid(row=0, column=0)
        tk.Scale(self, from_=-100, to=100, orient=tk.HORIZONTAL, label="Contrast").grid(row=1, column=0)
        tk.Scale(self, from_=-100, to=100, orient=tk.HORIZONTAL, label="Sharpness").grid(row=2, column=0)
        tk.Scale(self, from_=-100, to=100, orient=tk.HORIZONTAL, label="Saturation").grid(row=3, column=0)

        awb_var = tk.StringVar(self)
        awb_var.set(self.camera.awb_mode)
        tk.OptionMenu(self, awb_var, *self.camera.AWB_MODES, command=self.set_awb_mode).grid(row=1, column=1)

        meter_var = tk.StringVar(self)
        meter_var.set(self.camera.meter_mode)
        tk.OptionMenu(self, meter_var, *self.camera.METER_MODES, command=self.set_meter_mode).grid(row=2, column=1)

        exposure_var = tk.StringVar(self)
        exposure_var.set(self.camera.exposure_mode)
        tk.OptionMenu(self, exposure_var, *self.camera.EXPOSURE_MODES, command=self.set_exposure_mode)\
            .grid(row=3, column=1)

    def update_brightness(self, value):
        pass

    def update_contrast(self, value):
        pass

    def update_sharpness(self, value):
        pass

    def update_saturation(self, value):
        pass

    def set_awb_mode(self, awb_mode):
        """Set camera Auto White Balance"""
        self.camera.awb_mode = awb_mode

    def set_meter_mode(self, meter_mode):
        """Set camera meter mode"""
        self.camera.meter_mode = meter_mode

    def set_exposure_mode(self, exposure_mode):
        self.camera.exposure_mode = exposure_mode

    def set_shutter_speed(self, shutter_speed_value):
        """Set camera shutter speed"""
        self.camera.shutter_speed = shutter_speed_value

    def set_iso(self, iso_value):
        """Set camera ISO"""
        self.camera.iso = iso_value
