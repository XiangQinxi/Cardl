from Cardl.Lib.InterFace.Widgets.widget import CWidget
from tkwebview2 import tkwebview2
import customtkinter as ctk
import tkinter as tk


class CWebKit2(CWidget):
    def __init__(self, parent: CWidget = None, size=(30000, 30000), url: str = ""):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = tkwebview2.WebView2(parent, url=url, width=size[0], height=size[1])

    @property
    def webUrl(self):
        return self.widget.get_url()

    @webUrl.setter
    def webUrl(self, url: str):
        self.widget.load_url(url)

    @property
    def webHtml(self):
        return self.widget.get_url()

    @webHtml.setter
    def webHtml(self, content: str, baseUri: str = None):
        self.widget.load_html(content=content, base_uri=baseUri)

    def webReload(self):
        self.widget.reload()

    def checkRuntime(self):
        if not tkwebview2.have_runtime():
            tkwebview2.install_runtime()