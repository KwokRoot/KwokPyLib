# pyautogui 主要用于 鼠标、键盘、截屏控制。
# pip install pyautogui

import pyautogui
from pymsgbox import QUESTION


# 获取屏幕分辨率
print(pyautogui.size())

# 获取当前鼠标位置
p = pyautogui.position()
print(p.x)

# 取色
# print(pyautogui.pixel(1800, 15))


pyautogui.moveTo(1800, 15)
pyautogui.click()
# pyautogui.press("enter")


# 按顺序按下键，按相反的顺序释放键。
# pyautogui.hotkey('ctrl','shift','esc')


# # 消息框

# # 提示框
# print(pyautogui.alert(text='请知悉：用户协议', title='提示', button="OK"))
# # 确认框
# print(pyautogui.confirm(text='你确认删除吗？', title='提示', buttons=['OK', 'Cancel'], icon=QUESTION))
# # 输入框
# print(pyautogui.prompt(text='请输入', title='输入', default='确认'))
# # 密码框
# print(pyautogui.password(text='请输入密码', default='123', mask='*'))


# 输入字符
# pyautogui.moveTo(266, 729)
# pyautogui.click()
# pyautogui.write('hello world',interval=0.25)


# 截全屏
# pyautogui.screenshot("img.jpg")
# 截区域
# pyautogui.screenshot("img.jpg", region=(300, 400, 300, 100))


# 定位图片位置，需打开 `img.jpg`
# pyautogui.sleep(3)
# img_location = pyautogui.locateOnScreen('img.jpg', grayscale=True)
# print(img_location)


