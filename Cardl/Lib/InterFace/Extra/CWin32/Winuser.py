from ctypes import windll

winuser = windll.user32


def CloseWindow(*args, **kwargs):
    return winuser.CloseWindow(*args, **kwargs)

def GetParent(*args, **kwargs):
    return winuser.GetParent(*args, **kwargs)

def GetWindowText(*args, **kwargs):
    return winuser.GetWindowTextW(*args, **kwargs)

def SetWindowText(*args, **kwargs):
    return winuser.SetWindowTextW(*args, **kwargs)
