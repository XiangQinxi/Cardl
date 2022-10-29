from Cardl.Lib.InterFace.Widgets.widget import CWidget
from tkintermapview import TkinterMapView
import customtkinter as ctk
import tkinter as tk


class CMapKit(CWidget):
    def __init__(self, parent: CWidget = None, size=(30000, 30000), radius: int = 0, background: str = None, maxZoom: int = 19):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = TkinterMapView(parent, width=size[0], height=size[1], corner_radius=radius, max_zoom=maxZoom)

    @property
    def zoom(self):
        return self.widget.zoom

    @zoom.setter
    def zoom(self, value):
        self.widget.set_zoom(zoom=value)

    def address(self, address: str):
        self.widget.set_address(address_string=address)
