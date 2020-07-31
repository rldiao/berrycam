import tkinter as tk


class ModeNavBar:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.frame.grid(stick='sew')

        for col in range(3):
            tk.Grid.columnconfigure(self.frame, col, weight=1)

        photo_btn = tk.Button(self.frame, text='Photo').grid(row=0, column=0, stick='nsew')
        video_btn = tk.Button(self.frame, text='Video').grid(row=0, column=1, stick='nsew')
        setting_btn = tk.Button(self.frame, text='Setting').grid(row=0, column=2, stick='nsew')
