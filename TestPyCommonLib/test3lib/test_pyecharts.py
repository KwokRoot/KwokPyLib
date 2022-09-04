import os

import pyecharts
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.render import make_snapshot


# 查看包版本，官方参考文档：https://pyecharts.org
print(pyecharts.__version__)


# pyecharts 使用的静态资源，默认挂载在 https://assets.pyecharts.org/assets/
# CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"


x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]


line = Line()
line.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
                     toolbox_opts=opts.ToolboxOpts(is_show=True))
line.add_xaxis(x)
line.add_yaxis("Y轴", y)


# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件，可传入路径参数，如 line.render("echarts.html")。
# line.render("temp/echarts.html")


# HTML 输出到 图片
# 需要安装 snapshot-selenium，pip install snapshot-selenium
from snapshot_selenium import snapshot

# snapshot-selenium 需要配置 `chromedriver.exe` 路径到环境变量。
os.environ['PATH'] += ';D:\Kwok\Work\Other'
# print(os.environ['PATH'])

make_snapshot(snapshot, line.render("temp/echarts.html"), "temp/echarts.png")


