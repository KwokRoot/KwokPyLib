# pip install graphviz
import graphviz

# 无向图
# graphviz.Graph()

# 有向图
dot = graphviz.Digraph(
    name='示例图',
    comment='示例图',
    format='png',
    encoding='UTF-8',
    graph_attr={'fontname': 'Microsoft YaHei'},  # 图表级字体
    node_attr={'fontname': 'Microsoft YaHei', 'fontsize': '30'},  # 节点级字体
    edge_attr={'fontname': 'Microsoft YaHei'},  # 边级字体
    strict=True,  # 避免重复边
    engine='dot',
)

# 添加节点
dot.node('A', '节点A', color='yellow')
dot.node('B', '节点B')
dot.node('C', '节点C')

# 添加边
dot.edge('A', 'B', '依赖', color='red')
dot.edge('B', 'C', '依赖')
dot.edge('A', 'C', '依赖')
# dot.edge('A', 'C', '依赖')
dot.edge('C', 'A', '依赖', dir='none')

dot.node('X', '节点X', fontsize='22')
dot.node('Y', '节点Y', fontsize='22')
dot.node('Z', '节点Z', fontsize='22')

dot.edges(['XY', 'YZ', 'XZ'])

# 渲染图形
# dot.render('example_graph', view=True, cleanup=True, format='png')
dot.render('graph', view=True, format='png')

print(dot.source)


src = """
// 示例图
strict graph "示例图" {
	graph [fontname="Microsoft YaHei"]
	node [fontname="Microsoft YaHei" fontsize=30]
	edge [fontname="Microsoft YaHei"]
	X [label="节点X" fontsize=22]
	Y [label="节点Y" fontsize=22]
	Z [label="节点Z" fontsize=22]
	X -- Y
	Y -- Z
	X -- Z
}
"""

dot2 = graphviz.Source(src)
dot2.render('graph2', view=True, format='png')

