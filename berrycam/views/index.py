import tkinter as tk

from .control_bar import ControlBar
from .mode import ModeView
from .mode_navbar import ModeNavBar


class Index:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.parent.geometry("600x600")
        self.parent.title("BerryCam")

        tk.Grid.rowconfigure(self.parent, 0, weight=1)
        tk.Grid.columnconfigure(self.parent, 0, weight=1)

        mode_view = ModeView(self.parent).grid(sticky='nsew')
        ModeNavBar(self.parent, mode_view).grid(sticky='sew')
        ControlBar(self.parent).grid(sticky='nsew')

