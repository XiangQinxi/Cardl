from Cardl.Lib.InterFace.Widgets.window import CWindow
from typing import Literal


class WindowsEffect:
    systemBackDropType = Literal["None", "Auto"]

    def __init__(self, window: CWindow):
        self.window = window

    def setBorderColor(self, hex=None, rgb=None):
        from Cardl.Lib.InterFace.Extra.CWin32.Dwmapi import DwmSetWindowAttribute, DWMWA_BORDER_COLOR
        if hex is not None:
            DwmSetWindowAttribute(self.window.widgetHWND, DWMWA_BORDER_COLOR, self.window.hex(hex))
        elif rgb is not None:
            DwmSetWindowAttribute(self.window.widgetHWND, DWMWA_BORDER_COLOR, self.window.rgb(rgb[0], rgb[1], rgb[2]))

    def setTitleColor(self, hex=None, rgb=None):
        from Cardl.Lib.InterFace.Extra.CWin32.Dwmapi import DwmSetWindowAttribute, DWMWA_TEXT_COLOR
        if hex is not None:
            DwmSetWindowAttribute(self.window.widgetHWND, DWMWA_TEXT_COLOR, self.window.hex(hex))
        elif rgb is not None:
            DwmSetWindowAttribute(self.window.widgetHWND, DWMWA_TEXT_COLOR, self.window.rgb(rgb[0], rgb[1], rgb[2]))

    def setSystemBackDrop(self, value: str):
        from Cardl.Lib.InterFace.Extra.CWin32.Dwmapi import DwmSetWindowAttribute, DWMWA_SYSTEMBACKDROP_TYPE, DWMSBT_NONE, DWMSBT_AUTO

        if value == "None":
            value = DWMSBT_NONE
        elif value == "Auto":
            value = DWMSBT_AUTO

        DwmSetWindowAttribute(self.window.widgetHWND, DWMWA_SYSTEMBACKDROP_TYPE, value)
