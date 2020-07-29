import tkinter as tk


class PhotoFrame(tk.Frame):
    """
    Allows users to interact with PiCamera in a photo centric view
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.btn_frame = tk.Frame(self)
        self.btn_frame.grid(row=1, column=2, columnspan=2)

        tk.Button(self.btn_frame, text='Preview ON', command=self.preview_on).grid(row=1, column=1)
        tk.Button(self.btn_frame, text='Preview OFF', command=self.preview_off).grid(row=1, column=2)

        tk.Button(self.btn_frame, text='Take Photo', command=self.take_photo).grid(row=1, column=3)

    def preview_on(self):
        print('Preview - ON')

    def preview_off(self):
        print('Preview - OFF')

    def take_photo(self):
        print('Snap!')
