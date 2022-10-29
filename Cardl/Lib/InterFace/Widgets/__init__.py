from Cardl.Lib.InterFace.Widgets.thememanager import CThemeManager
from Cardl.Lib.InterFace.Widgets.application import CApplication
from Cardl.Lib.InterFace.Widgets.eventhandle import *
from Cardl.Lib.InterFace.Widgets.widget import CWidget
from Cardl.Lib.InterFace.Widgets.window import CWindow, EVTX_DELETE_WINDOW, EVTX_TAKE_FOCUS
from Cardl.Lib.InterFace.Widgets.panel import CPanel
from Cardl.Lib.InterFace.Widgets.button import CButton
from Cardl.Lib.InterFace.Widgets.combobox import CComboBox
from Cardl.Lib.InterFace.Widgets.entry import CEntry


def DefaultRoot():
    from tkinter import _default_root
    window = CWindow()
    window.modifyWidget(_default_root)
    return window