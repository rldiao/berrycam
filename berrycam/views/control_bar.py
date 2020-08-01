import tkinter as tk

from berrycam.camera import camera_provider


class ControlBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.camera = camera_provider()
        self.parent = parent
        self['padx'] = 10
        self['pady'] = 10

        for col in range(3):
            tk.Grid.columnconfigure(self, col, weight=1)

        preview_btn = tk.Button(self, text='Preview', width=20, command=self.preview_toggle)
        preview_btn.grid(row=0, column=0, columnspan=1, stick='nsew')

        capture_btn = tk.Button(self, text='Capture', width=20, command=self.capture)
        capture_btn.grid(row=0, column=1, columnspan=1, stick='nsew')

        settings_btn = tk.Button(self, text='Settings', width=20)
        settings_btn.grid(row=0, column=2, columnspan=1, stick='nsew')

    def preview_toggle(self):
        """Toggle Camera Preview"""
        if self.camera.preview is None:
            self.camera.start_preview()
        else:
            self.camera.stop_preview()

    def capture(self):
        """Capture with Camera"""
        self.camera.capture()
