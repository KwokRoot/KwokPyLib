from turtle import *


# 画五角星
def draw_star(x, y):
    # penup 提笔，移动路径不画出来
    pu()
    # 画笔移动到坐标位置，注：画笔初始位置为画布中心，方向向右
    goto(x, y)
    # pendown 落笔，移动路径画出来
    pd()
    # 设置当前画笔朝向某角度
    seth(0)
    # 开始填充
    begin_fill()
    for i in range(5):
        # 向当前画笔方向移动
        fd(45)
        # 画笔方向顺时针旋转度数
        rt(144)
    # 结束填充
    end_fill()


# 画布在屏幕大小、位置
setup(0.8, 0.6)
# 画布大小、颜色
screensize(300, 200, "ivory")
# 初始化画笔粗细
pensize(3)
# 画笔速度
speed(1000)
# 画笔颜色
pencolor("red")
# 填充颜色
fillcolor("yellow")


for x in range(-125, 125, 50):
    draw_star(x, 0)


# 隐藏画笔形状
hideturtle()
# 画布窗口不自动退出
# done()

print("ok")

