from Cardl.Lib.InterFace.Widgets.widget import CWidget
import customtkinter as ctk
import tkinter as tk


class CFrame(CWidget):
    def __init__(self, parent: CWidget = None, *args, **kwargs):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = ctk.CTkFrame(parent, *args, **kwargs)


if __name__ == '__main__':
    from Cardl.BaseUi import CWindow, CApplication
    application = CApplication()
    window = CWindow()
    frame = CFrame(window)
    frame.widgetPack(fill="both", expand="yes", padx=10, pady=10)
    application.run(window)