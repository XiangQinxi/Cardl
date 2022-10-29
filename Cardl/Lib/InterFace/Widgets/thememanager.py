import customtkinter as ctk


class CThemeManager(object):
    def __init__(self):
        self.widget = ctk.theme_manager.ThemeManager()

    @property
    def theme(self):
        return self.widget.theme

    @property
    def themeColor(self):
        return self.theme["color"]