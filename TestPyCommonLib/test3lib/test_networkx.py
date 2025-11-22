# pip install networkx
import networkx as nx

g = nx.DiGraph()
# 添加节点
g.add_node('Z')
# 批量添加节点
g.add_nodes_from([1, 2, 3])
# 添加关系
g.add_edge('X', 'Y')
# 批量添加关系
g.add_edges_from([(1, 2), (1, 3), (2, 3)])

# 网络图绘制与显示
import matplotlib.pyplot as plt

nx.draw(g, with_labels=True)
plt.show()


# 导出 pydot 图结构
# pip install pydot
# from networkx.drawing.nx_pydot import to_pydot

# print(to_pydot(g))

# 导出 graphviz 图结构
# pip install pygraphviz
# from networkx.drawing.nx_agraph import to_agraph

# print(to_agraph(g))

