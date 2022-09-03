import time

# 依赖 `pywin32` 库，主要使用到 Application 类，用于应用程序管理（打开与关闭应用等）、窗口管理（最小化、最大化、关闭窗口）
# pip install pywinauto
from pywinauto.application import Application

app = Application(backend="uia")

app.start(r"notepad.exe")

win = app["无标题 - 记事本"]
win.menu_select('帮助 -> 关于记事本')
app["Dialog"]["确定"].click()

win["Edit"].set_text("hello world.")
win.type_keys("123")
time.sleep(2)
app.kill()


