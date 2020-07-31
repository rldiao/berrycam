import tkinter as tk

from .control_bar import ControlBar
from .mode_navbar import ModeNavBar


class Index:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.parent.geometry("320x300")
        self.parent.title("BerryCam")

        for row_index in range(2):
            tk.Grid.rowconfigure(self.parent, row_index, weight=1)
            for col in range(1):
                tk.Grid.columnconfigure(self.parent, col, weight=1)

        main = tk.Frame(self.parent, bg='red', height='300', width='300').grid(row=0, column=0)
        ModeNavBar(self.parent)
        ControlBar(self.parent)

