from ctypes import windll

dwmapi = windll.dwmapi


DWMSBT_AUTO = 0
DWMSBT_NONE = 1
DWMSBT_MAINWINDOW = 2
DWMSBT_TRANSIENTWINDOW = 3
DWMSBT_TABBEDWINDOW = 4

DWMNCRP_USEWINDOWSTYLE = 0
DWMNCRP_DISABLED = 1
DWMNCRP_ENABLED = 2
DWMNCRP_LAS = 3

DWMWCP_DEFAULT = 0
DWMWCP_DONOTROUND = 1
DWMWCP_ROUND = 2
DWMWCP_ROUNDSMALL = 3

DWM_BB_ENABLE = 0x00000001
DWM_BB_BLURREGION = 0x00000002
DWM_BB_TRANSITIONONMAXIMIZED = 0x00000004

DWMWA_NCRENDERING_ENABLED = 1
DWMWA_NCRENDERING_POLICY = 2
DWMWA_TRANSITIONS_FORCEDISABLED = 3
DWMWA_ALLOW_NCPAINT = 4
DWMWA_CAPTION_BUTTON_BOUNDS = 5
DWMWA_NONCLIENT_RTL_LAYOUT = 6
DWMWA_FORCE_ICONIC_REPRESENTATION = 7
DWMWA_FLIP3D_POLICY = 8
DWMWA_EXTENDED_FRAME_BOUNDS = 9
DWMWA_HAS_ICONIC_BITMAP = 10
DWMWA_DISALLOW_PEEK = 11
DWMWA_EXCLUDED_FROM_PEEK = 12
DWMWA_CLOAK = 13
DWMWA_CLOAKED = 14
DWMWA_FREEZE_REPRESENTATION = 15
DWMWA_PASSIVE_UPDATE_MODE = 16
DWMWA_USE_HOSTBACKDROPBRUSH = 17
DWMWA_CAPTION_COLOR = 19
DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_LAST = 24
DWMWA_WINDOW_CORNER_PREFERENCE = 33
DWMWA_BORDER_COLOR = 34
DWMWA_TEXT_COLOR = 36
DWMWA_VISIBLE_FRAME_BORDER_THICKNESS = 37
DWMWA_SYSTEMBACKDROP_TYPE = 38

DWMSC_DOWN = 0
DWMSC_UP = 1
DWMSC_DRAG = 2
DWMSC_HOLD = 3
DWMSC_PENBARREL = 4
DWMSC_NONE = 5
DWMSC_ALL = 6


def DwmSetWindowAttribute(hWnd, attribute, value):
    from ctypes import wintypes
    from ctypes import byref, c_int, sizeof

    value = c_int(value)
    dwmapi.DwmSetWindowAttribute(hWnd, attribute, byref(value), sizeof(value))