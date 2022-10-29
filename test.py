from Cardl.BaseUi import *


Application = CApplication()
Application.setAppearance("Dark")

Window = CWindow()

ComBoBox = CComboBox(values=("Hello"))
ComBoBox.widgetStartBoxV(padx=10, pady=10)

Button = CButton(onClick=lambda: print("Hello World"))
Button.widgetStartBoxV(padx=10, pady=10)

Entry = CEntry()
Entry.widgetPack(padx=10, pady=10)

Application.run(Window)
