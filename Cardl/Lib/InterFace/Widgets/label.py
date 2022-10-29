from Cardl.Lib.InterFace.Widgets.widget import CWidget
import customtkinter as ctk
import tkinter as tk


class CLabel(CWidget):
    def __init__(self, parent: CWidget = None, text: str = "", *args, **kwargs):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = ctk.CTkLabel(parent, text=text, *args, **kwargs)

    @property
    def labelText(self):
        return self.widget.text

    @labelText.setter
    def labelText(self, text: str):
        self.widget.set_text(text)


if __name__ == '__main__':
    from Cardl.BaseUi import CWindow, CApplication
    application = CApplication()
    window = CWindow()
    label = CLabel(window, text="Hello World")
    label.widgetPack()
    application.run(window)