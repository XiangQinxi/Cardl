from Cardl.Lib.InterFace.Widgets.window import CWindow
from Cardl.Lib.InterFace.Images import EmptyIcon
import customtkinter as ctk


class CPanel(CWindow):
    def __init__(self, parent: CWindow, *args, title: str = "", **kwargs):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = ctk.CTkToplevel(parent, *args, **kwargs)
        self.windowTitle = title
        self.widget.appearance_mode
        try:
            self.windowIcon = EmptyIcon
        except:
            pass