# fleter
一个flet的扩展组件库，提供一些常用组件及功能。

## ComboBox
用于简化`Dropdown`的开发过程，`option`可以使用列表设置，如`["Hello", "World"]`。

![](https://xiangqinxi-development-resourse.netlify.app/_downloads/cdce347339a24c65eba9ab74cf25c918/ComboBox.gif)
```python
import flet
import fleter


def build(page: flet.Page):
    item = []
    for index in range(20):
        item.append(f"item{index}")
    page.add(fleter.ComboBox(options=item))
    page.update()

flet.app(target=build)
```

## Editor
文本编辑器。
```python
import flet
import fleter


def build(page: flet.Page):
    editor = fleter.Editor()
    
    page.add(editor)
    page.add(fleter.ComboBox(options=item))
    page.update()

flet.app(target=build)
```

## HeaderBar
用于快速设置窗口标题栏。

![](https://xiangqinxi-development-resourse.netlify.app/_downloads/7a47bcc3bf6ba9d1cb1bbd90eaa43194/HeaderBar-Title-Left.gif)

### 常规
```python
import flet
import fleter


def build(page: flet.Page):
    titlebar = fleter.HeaderBar(page, title="Hello World")
    page.add(
        titlebar
    )
    page.update()

flet.app(target=build)
```

### 标题栏靠左-切换主题按钮

```python
import flet
import fleter


def build(page: flet.Page):
    titlebar = fleter.HeaderBar(page, title="Hello World", title_align="left")
    titlebar.controls.insert(1, fleter.SwichThemeButton(page))
    page.add(
        titlebar
    )
    page.update()

flet.app(target=build)
```

### 获取标题栏里面的关闭按钮
可以在组件中找到`close_button`的属性，并对其进行设置。（前提是设置`has_close`属性为`True`）
```python
import flet
import fleter


def build(page: flet.Page):
    titlebar = fleter.HeaderBar(page)
    print(titlebar.close_button)
    page.add(
        titlebar
    )
    page.update()

flet.app(target=build)
```

### 设置是否有关闭按钮
我们知道`HeaderBar`初始化时有个`has_close`的属性，如果需要在后面设置是否有关闭按钮时，就可以调用`has_close`属性进行设置
```python
import flet
import fleter


def build(page: flet.Page):
    titlebar = fleter.HeaderBar(page)
    titlebar.close_button = False  # True保留关闭按钮，False不保留关闭按钮
    page.add(
        titlebar
    )
    page.update()

flet.app(target=build)
```

## SwichThemeButton
用于快速切换窗口主题的图标按钮组件。

### 常规

![](https://xiangqinxi-development-resourse.netlify.app/_downloads/66614d49add24beda5ebe2d69c3f8196/SwichThemeButton.gif)
```python
import flet
import fleter

def main(page: flet.Page):
    swich_theme_button = fleter.SwichThemeButton(page)
    page.add(
        swich_theme_button
    )
    page.update()

flet.app(target=main)
```

### 无系统主题选项

![](https://xiangqinxi-development-resourse.netlify.app/_downloads/65429c27320025ae1eeb32137d6a22e1/SwichThemeButton-None-System.gif)
```python
import flet
import fleter

def main(page: flet.Page):
    swich_theme_button = fleter.SwichThemeButton(page, has_system=False)
    page.add(
        swich_theme_button
    )
    page.update()

flet.app(target=main)
```

## SphinBox
进步器，用于调整整数或浮点数的数值

![](https://xiangqinxi-development-resourse.netlify.app/_downloads/a30e33a93f13e0703ad5df21e0089217/SphinBox.gif)
```python
import flet
import fleter

def main(page: flet.Page):
    page.add(
        fleter.SphinBox()
    )
    page.update()

flet.app(target=main)
```

### 浮点数步进器

![](https://xiangqinxi-development-resourse.netlify.app/_downloads/2b1755911a97f23adf284622f8d01a8b/SphinBox-Float.gif)
```python
import flet
import fleter

def main(page: flet.Page):
    page.add(
        fleter.SphinBox(plus=0.1, minus=0.1)
    )
    page.update()

flet.app(target=main)
```

### 最大值与最小值
设置步进器可设置的最大值。

![](https://xiangqinxi-development-resourse.netlify.app/_downloads/067605165c9c1ca5c335948adaca74cc/SphinBox-Max-Min.gif)
```python
import flet
import fleter

def main(page: flet.Page):
    page.add(
        fleter.SphinBox(max_value=5, min_value=-5)
    )
    page.update()

flet.app(target=main)
```

## Time
使用`threading`库做出来的记时工具。
```python
import flet
import fleter

def main(page: flet.Page):

    def tick(id, tick_time):
        print(f"{id} {tick_time}")

    time = fleter.Time(tick)
    time.start("time", 10)

    page.update()

flet.app(target=main)
```