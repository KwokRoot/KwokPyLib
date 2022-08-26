from matplotlib import pyplot as plot

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]


# 折线图标题
plot.title("测试图")
# 支持中文
plot.rcParams['font.sans-serif'] = ['SimHei']
# X轴标题
plot.xlabel('X 轴')
# Y轴标题
plot.ylabel('Y 轴')

# 图片像素
plot.rcParams['savefig.dpi'] = 100
# 分辨率
plot.rcParams['figure.dpi'] = 100

# 去除白边
plot.margins(0, 0)

# 不显示坐标轴
# plot.axis("off")

# 不显示 X轴数值
# plot.xticks([])
# 不显示 Y轴数值
# plot.yticks([])

plot.plot(x, y, c='red')

plot.savefig("/opt/plot.jpg", format="jpg")
# 清除当前画板
# plot.cla()

plot.show()
