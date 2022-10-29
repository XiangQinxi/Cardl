from Cardl.Lib.Object import CObject
from Cardl.Lib.InterFace.Widgets.eventhandle import CEventHandle
import customtkinter as ctk
import tkinter as tk
from typing import Literal


class CWidget(CEventHandle, CObject):
    def __init__(self):
        try:
            self.widget = tk.Widget()
        except:
            pass

    appearanceType = Literal["Light", "Dark", "System"]

    @property
    def widgetFocus(self):
        return self.widget.focus_get()

    @widgetFocus.setter
    def widgetFocus(self, focus: bool = True):
        if focus:
            self.widget.focus_get()

    def widgetApplyMica(self, isDark: bool = False):
        from win32mica import ApplyMica
        ApplyMica(self.widgetHWND, isDark)

    def widgetDestroy(self):
        self.widget.destroy()

    @property
    def widgetBackground(self):
        return self.widget.cget("background")

    @widgetBackground.setter
    def widgetBackground(self, color):
        self.widget.configure(background=color)

    @property
    def widgetForeground(self):
        return self.widget.cget("foreground")

    @widgetForeground.setter
    def widgetForeground(self, color):
        self.widget.configure(foreground=color)

    def modifyWidget(self, widget):
        self.widget = widget

    @property
    def allAppearance(self):
        return ctk.get_appearance_mode()

    @allAppearance.setter
    def allAppearance(self, appearance: appearanceType):
        self.set("allAppearance", appearance)
        ctk.set_appearance_mode(appearance)

    def widgetAttribute(self, attribute_name: str, attribute_value=None):
        if attribute_value is None:
            return self.widget.cget(attribute_name)
        eval(f"self.widget.configure({attribute_name}={attribute_value})")

    def widgetAttributeX(self, attribute_name: str, attribute_value=None):
        if attribute_value is None:
            return self.widget

    def widgetBell(self):
        self.widget.bell()

    @property
    def widgetWidth(self):
        return self.widget.winfo_width()

    @property
    def widgetHeight(self):
        return self.widget.winfo_height()

    def widgetUpdate(self):
        self.widget.update()

    @property
    def widgetAppearance(self):
        return self.widget.appearance_mode

    @widgetAppearance.setter
    def widgetAppearance(self, appearance: appearanceType):
        self.widget.set_appearance_mode(appearance)

    @property
    def widgetID(self):
        return self.widget.winfo_id()

    @property
    def widgetHWND(self):
        from sys import platform
        if platform == "win32":
            from Cardl.Lib.InterFace.Extra.CWin32.Winuser import GetParent
            return GetParent(self.widgetID)

    def widgetPack(self, *args, **kwargs):
        self.widget.pack(*args, **kwargs)

    def widgetPlace(self, *args, **kwargs):
        self.widget.place(*args, **kwargs)

    def widgetGrid(self, *args, **kwargs):
        self.widget.grid(*args, **kwargs)

    def widgetStartBoxV(self, *args, **kwargs):
        self.widgetPack(side="top", *args, **kwargs)

    def widgetEndBoxV(self, *args, **kwargs):
        self.widgetPack(side="bottom", *args, **kwargs)

    @property
    def widgetContentBackground(self):
        return self.widget.fg_color

    @widgetContentBackground.setter
    def widgetContentBackground(self, color):
        self.widget.configure(fg_color=color)

    @property
    def widgetContentForeground(self):
        return self.widget.fg_color

    @widgetContentForeground.setter
    def widgetContentForeground(self, color):
        self.widget.configure(text_color=color)

    @property
    def widgetContentBorderColor(self):
        return self.widget.border_color

    @widgetContentBorderColor.setter
    def widgetContentBorderColor(self, color):
        self.widget.configure(border_color=color)

    @property
    def widgetContentBorderWidth(self):
        return self.widget.borderwidth

    @widgetContentBorderWidth.setter
    def widgetContentBorderWidth(self, width):
        self.widget.configure(borderwidth=width)