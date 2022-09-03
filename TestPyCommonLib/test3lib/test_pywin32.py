# pywin32：包含 win32gui、win32api、win32con 3个子模块
# 用于窗口管理（定位窗口、显示和关闭窗口、获取窗口位置等）, 更底层，操作较复杂。
# pip install pypiwin32
import time

import win32api
import win32con
import win32gui


# 消息框
# print(win32api.MessageBox(None, "Hello, pywin32!", "pywin32", win32con.MB_ICONWARNING))

# 鼠标操作
# 显示缩放百分比
factor = 1.25
win32api.SetCursorPos((int(1777/factor), int(25/factor)))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 获取最前窗口句柄
time.sleep(2)
hwnd = win32gui.GetForegroundWindow()
print(hwnd)

# 获取窗口标题
title = win32gui.GetWindowText(hwnd)
print(title)

# 通过类名(参数1)或标题(参数2)查找窗口，获取最前窗口的标题、类名、位置大小
hwnd = win32gui.FindWindow(None, title)
print(win32gui.GetWindowText(hwnd))
print(win32gui.GetClassName(hwnd))
print(win32gui.GetWindowRect(hwnd))
win32gui.CloseWindow(hwnd)


hwnd = win32gui.FindWindowEx(0, 0, "MozillaWindowClass", None)
print(win32gui.GetWindowText(hwnd))
win32gui.CloseWindow(hwnd)

