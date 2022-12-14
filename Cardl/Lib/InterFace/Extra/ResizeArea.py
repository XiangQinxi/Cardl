from tkinter import Canvas
from functools import partial
from Cardl.Lib.InterFace.Widgets.widget import CWidget


class SelectedCanvas(Canvas):
    """可调整组件大小、可移动的画布"""

    def __init__(self, master=None, borderColor="#006eb8", arrowColor="#0099ff", cnf={}, **kw):
        Canvas.__init__(self, master, cnf, **kw)
        self.config(bd=0, highlightthickness=0, background="#ffffff")
        self.is_sizing = False
        self.old_width = 0
        self.old_height = 0
        self.old_pos_x = 0
        self.old_pos_y = 0
        self.start_x = 0
        self.start_y = 0
        self.start_root_x = 0
        self.start_root_y = 0
        self.on_resize_complete = None
        self.have_child = False

        self.border_color = borderColor
        self.arrow_color = arrowColor

    def _mousedown(self, event):
        self.startx = event.x
        self.starty = event.y

    def _drag(self, event):
        try:
            self.place(x=self.winfo_x() + (event.x - self.startx), y=self.winfo_y() + (event.y - self.starty))
        except AttributeError:
            raise ValueError("The widget %s is not draggable" % widget)

    def set_on_resize_complete(self, on_resize_complete):
        self.on_resize_complete = on_resize_complete

    def on_update(self):
        self.create_rectangle(-1, -1, -2, -2, tag='side', dash=3, outline=self.border_color)
        self.tag_bind('side', "<Button-1>", self._mousedown, add='+')
        self.tag_bind('side', "<B1-Motion>", self._drag, add='+')
        self.tag_bind('side', '<Enter>', lambda event: self.config(cursor='fleur'))
        self.tag_bind('side', '<Leave>', lambda event: self.config(cursor='arrow'))
        for name in ('nw', 'w', 'sw', 'n', 's', 'ne', 'e', 'se'):
            self.create_rectangle(-1, -1, -2, -2, tag=name, outline=self.arrow_color)
            self.tag_bind(name, "<Enter>", partial(self.on_mouse_enter, name))
            self.tag_bind(name, "<Leave>", partial(self.on_mouse_leave, name))
            self.tag_bind(name, "<Button-1>", partial(self.on_mouse_click, name))
            self.tag_bind(name, "<B1-Motion>", partial(self.on_mouse_move, name))
            self.tag_bind(name, "<ButtonRelease-1>", partial(self.on_mouse_release, name))

    def setBorderColor(self, color):
        self.border_color = color

    def setArrowColor(self, color):
        self.arrow_color = color

    def show(self, is_fill=False):
        width = self.winfo_width()
        height = self.winfo_height()
        self.coords('side', 6, 6, width - 6, height - 6)
        self.coords('nw', 0, 0, 7, 7)
        self.coords('sw', 0, height - 8, 7, height - 1)
        self.coords('w', 0, (height - 7) / 2, 7, (height - 7) / 2 + 7)
        self.coords('n', (width - 7) / 2, 0, (width - 7) / 2 + 7, 7)
        self.coords('s', (width - 7) / 2, height - 8, (width - 7) / 2 + 7, height - 1)
        self.coords('ne', width - 8, 0, width - 1, 7)
        self.coords('se', width - 8, height - 8, width - 1, height - 1)
        self.coords('e', width - 8, (height - 7) / 2, width - 1, (height - 7) / 2 + 7)
        if is_fill:
            for name in ('nw', 'w', 'sw', 'n', 's', 'ne', 'e', 'se'):
                self.itemconfig(name, fill='blue')

    def hide(self):
        self.coords('side', -1, -1, -2, -2, )
        for name in ('nw', 'w', 'sw', 'n', 's', 'ne', 'e', 'se'):
            self.coords(name, -1, -1, -2, -2)

    def on_mouse_enter(self, tag_name, event):
        if tag_name in ("nw", "sw", "ne", "se"):
            self["cursor"] = "sizing"
        elif tag_name in ("w", "e"):
            self["cursor"] = "sb_h_double_arrow"
        else:
            self["cursor"] = "sb_v_double_arrow"

    def on_mouse_leave(self, tag_name, event):
        if self.is_sizing:
            return
        self["cursor"] = "arrow"

    def on_mouse_click(self, tag_name, event):
        self.is_sizing = True
        self.start_x = event.x
        self.start_y = event.y
        self.start_root_x = event.x_root
        self.start_root_y = event.y_root
        self.old_width = self.winfo_width()
        self.old_height = self.winfo_height()
        self.old_pos_x = int(self.place_info()['x'])
        self.old_pos_y = int(self.place_info()['y'])

    def on_mouse_move(self, tag_name, event):
        if not self.is_sizing:
            return
        if 'e' in tag_name:
            width = max(0, self.old_width + (event.x - self.start_x))
            self.place_configure(width=width)
        if 'w' in tag_name:
            width = max(0, self.old_width + (self.start_root_x - event.x_root))
            to_x = event.x - self.start_x + int(self.place_info()['x'])
            self.place_configure(width=width, x=to_x)
        if 's' in tag_name:
            height = max(0, self.old_height + (event.y - self.start_y))
            self.place_configure(height=height)
        if 'n' in tag_name:
            height = max(0, self.old_height + (self.start_root_y - event.y_root))
            to_y = event.y - self.start_y + int(self.place_info()['y'])
            self.place_configure(height=height, y=to_y)
        self.after_idle(self.show)

    def on_mouse_release(self, tag_name, event):
        self.is_sizing = False
        if self.on_resize_complete is not None:
            self.on_resize_complete()
        self["cursor"] = "arrow"

    def create_widget(self, widget: CWidget):
        if self.have_child:
            return
        self.have_child = True
        self.widget = widget
        self.widget.widgetPack(fill='both', expand=True, ipadx=9, ipady=9)
        # 即使拖动组件，也可以移动
        self.widget.bindEvent("<Button-1>", self.mousedown, add='+')
        self.widget.bindEvent("<B1-Motion>", self.drag, add='+')
        self.widget.bindEvent('<FocusOut>', lambda event: self.delete('all'))
        self.widget.bindEvent('<FocusIn>', lambda event: (self.on_update(), self.show()))

    def mousedown(self, event):
        self.widget.widgetFocus = True
        self.__startx = event.x
        self.__starty = event.y

    def drag(self, event):
        self.place(x=self.winfo_x() + (event.x - self.__startx), y=self.winfo_y() + (event.y - self.__starty))


class ResizeArea(CWidget):
    def __init__(self, parent: CWidget = None, borderColor: str = "#006eb8", arrowColor: str = "#0099ff"):
        super().__init__()
        if parent is None:
            parent = None
        else:
            parent = parent.widget
        self.widget = SelectedCanvas(parent, borderColor=borderColor, arrowColor=arrowColor)

    def setBorderColor(self, color):
        self.widget.setBorderColor(color)

    def setArrowColor(self, color):
        self.widget.setArrowColor(color)

    def addWidget(self, widget: CWidget):
        self.widget.create_widget(widget)

