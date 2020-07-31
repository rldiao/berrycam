import tkinter as tk


class ControlBar:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.frame = tk.Frame(self.parent, padx=10, pady=10)
        self.frame.grid(stick='nsew')

        for col in range(3):
            tk.Grid.columnconfigure(self.frame, col, weight=1)

        photo_btn = tk.Button(self.frame, text='Playback', width=20)
        photo_btn.grid(row=0, column=0, columnspan=1, stick='nsew')

        video_btn = tk.Button(self.frame, text='Snap', width=20)
        video_btn.grid(row=0, column=1, columnspan=1, stick='nsew')

        settings_btn = tk.Button(self.frame, text='Settings', width=20)
        settings_btn.grid(row=0, column=2, columnspan=1, stick='nsew')
