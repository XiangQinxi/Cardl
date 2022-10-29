from Cardl.Lib.InterFace.Widgets.widget import CWidget
from Cardl.Lib.InterFace.Images import EmptyIcon
import customtkinter as ctk


EVTX_DELETE_WINDOW = "WM_DELETE_WINDOW"
EVTX_TAKE_FOCUS = "WM_TAKE_FOCUS"


class CWindow(CWidget):
    def __init__(self, *args, title: str = "", **kwargs):
        super().__init__()
        self.widget = ctk.CTk(*args, **kwargs)
        self.windowTitle = title
        self.widget.appearance_mode
        try:
            self.windowIcon = EmptyIcon
        except:
            pass

    def bindEventX(self, eventName: str = None, eventFunc=None):
        self.widget.protocol(eventName, eventFunc)

    def onDeleteWindow(self, eventFunc=None):
        self.bindEventX(EVTX_DELETE_WINDOW, eventFunc)

    @property
    def windowAlpha(self):
        return self.widget.attributes("-alpha")

    @windowAlpha.setter
    def windowAlpha(self, alpha: float = 1):
        self.widget.attributes("-alpha", alpha)

    @property
    def windowIcon(self):
        return self.widget.iconbitmap()

    @windowIcon.setter
    def windowIcon(self, file):
        self.widget.iconbitmap(file)

    def windowRun(self):
        self.widget.mainloop()

    @property
    def windowRemoveTitleBar(self):
        return self.widget.overrideredirect()

    @windowRemoveTitleBar.setter
    def windowRemoveTitleBar(self, remove: bool):
        self.widget.overrideredirect(remove)

    @property
    def windowScaling(self):
        return self.widget.window_scaling

    @windowScaling.setter
    def windowScaling(self, scale: float):
        self.widget.apply_window_scaling(scale)

    @property
    def windowTitle(self) -> str:
        return self.widget.title()

    @windowTitle.setter
    def windowTitle(self, title: str) -> None:
        self.widget.title(title)

    def windowTitleBarDrag(self, widget: CWidget):
        for item in widget:
            pass

    @property
    def windowTransparentColor(self):
        return self.widget.attributes("-transparentcolor")

    @windowTransparentColor.setter
    def windowTransparentColor(self, color):
        self.widget.attributes("-transparentcolor", color)


if __name__ == '__main__':
    window = CWindow()
    window.windowRun()