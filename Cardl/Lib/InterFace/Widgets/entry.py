from Cardl.Lib.InterFace.Widgets.widget import CWidget
import customtkinter as ctk
import tkinter as tk


class CEntry(CWidget):
    def __init__(self, parent: CWidget = None, text: str = "", *args, **kwargs):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.text = tk.StringVar()
        self.text.set(text)
        self.widget = ctk.CTkEntry(parent, textvariable=self.text, *args, **kwargs)

    @property
    def entryText(self):
        return self.text.get()

    @entryText.setter
    def entryText(self, text: str):
        self.text.set(text)


if __name__ == '__main__':
    from Cardl.BaseUi import CWindow, CApplication
    application = CApplication()
    window = CWindow()
    label = CLabel(window, text="Hello World")
    label.widgetPack()
    application.run(window)