from Cardl.Lib.InterFace.Widgets.widget import CWidget
import customtkinter as ctk
import tkinter as tk


class CComboBox(CWidget):
    def __init__(self, parent: CWidget = None, *args, **kwargs):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = ctk.CTkComboBox(*args, **kwargs)
