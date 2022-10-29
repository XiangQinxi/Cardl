from Cardl.Lib.Object import CObject
from Cardl.Lib.InterFace.Widgets.window import CWindow
from Cardl.Lib.InterFace.StyleSheet import CardiTempTheme
from typing import Literal
import customtkinter as ctk


class CApplication(CObject):
    appearanceType = Literal["Light", "Dark", "System"]

    def __init__(self):
        self.setTheme(CardiTempTheme)

    def run(self, window: CWindow):
        window.windowRun()

    def setTheme(self, theme: str):
        ctk.set_default_color_theme(theme)

    def setAppearance(self, mode: appearanceType):
        ctk.set_appearance_mode(mode)
