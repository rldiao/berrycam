import tkinter as tk


class ExposureFrame(tk.Frame):
    choices = ['off', 'auto', 'sunlight', 'cloudy', 'shade', 'tungsten', 'fluorescent', 'incandescent', 'flash',
               'horizon']

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.btn_frame = tk.Frame(self)
        self.btn_frame.grid(row=5, column=3, columnspan=2)

        tk.Scale(self.btn_frame, from_=30, to=100, orient=tk.HORIZONTAL, label="Brightness",
                 command=self.update_brightness).grid(row=2, column=1)
        tk.Scale(self.btn_frame, from_=-100, to=100, orient=tk.HORIZONTAL, label="Contrast",
                 command=self.update_contrast).grid(row=2, column=2)
        tk.Scale(self.btn_frame, from_=-100, to=100, orient=tk.HORIZONTAL, label="Sharpness",
                 command=self.update_sharpness).grid(row=2, column=3)
        tk.Scale(self.btn_frame, from_=-100, to=100, orient=tk.HORIZONTAL, label="Saturation",
                 command=self.update_saturation).grid(row=3, column=1)
        tk.Scale(self.btn_frame, from_=10, to=99, orient=tk.HORIZONTAL, label="Zoom", command=self.zoom)\
            .grid(row=4, column=1)

        awb_var = tk.StringVar(self)
        awb_var.set(self.choices[0])
        tk.OptionMenu(self.btn_frame, awb_var, *self.choices, command=self.set_awb).grid(row=3, column=2)

    def update_brightness(self, value):
        pass

    def update_contrast(self, value):
        pass

    def update_sharpness(self, value):
        pass

    def update_saturation(self, value):
        pass

    def set_awb(self, var):
        print(var)

    def zoom(self, var):
        pass

