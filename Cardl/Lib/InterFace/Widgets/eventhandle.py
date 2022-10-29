EVT_LEFT_BUTTON = "<Button-1>"
EVT_MIDDLE_BUTTON = "<Button-2>"
EVT_RIGHT_BUTTON = "<Button-3>"

EVT_ENTER = "<Enter>"
EVT_LEAVE = "<Leave>"


class CEventHandle(object):
    def bindEvent(self, eventName, eventFunc, add=None):
        return self.widget.bind(eventName, eventFunc, add=add)

    def unbindEvent(self, eventName, eventID=None):
        self.widget.unbind(eventName)
