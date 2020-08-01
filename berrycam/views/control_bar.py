import tkinter as tk


class ControlBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.parent = parent
        self['padx'] = 10
        self['pady'] = 10

        for col in range(3):
            tk.Grid.columnconfigure(self, col, weight=1)

        photo_btn = tk.Button(self, text='Playback', width=20)
        photo_btn.grid(row=0, column=0, columnspan=1, stick='nsew')

        video_btn = tk.Button(self, text='Snap', width=20)
        video_btn.grid(row=0, column=1, columnspan=1, stick='nsew')

        settings_btn = tk.Button(self, text='Settings', width=20)
        settings_btn.grid(row=0, column=2, columnspan=1, stick='nsew')
