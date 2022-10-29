from Cardl.Lib.InterFace.Widgets.widget import CWidget
import customtkinter as ctk
import tkinter as tk


class CButton(CWidget):
    def __init__(self, parent: CWidget = None, text: str = "", onClick=None, *args, **kwargs):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = ctk.CTkButton(parent, text=text, command=onClick, *args, **kwargs)

    def onClick(self, func):
        self.widget.configure(command=func)

    @property
    def buttonText(self):
        return self.widget.text

    @buttonText.setter
    def buttonText(self, text: str):
        self.widget.set_text(text)

if __name__ == '__main__':
    from Cardl.BaseUi import CWindow, CApplication
    application = CApplication()
    window = CWindow()
    button = CButton(window, text="Hello World")
    button.widgetPack()
    application.run(window)