from collections import ChainMap

'''
# ChainMap 使用场景：
#   默认配置和覆盖配置：可以使用 ChainMap 将默认配置和覆盖配置组合起来。默认配置存储在一个字典中，覆盖配置存储在另一个字典中。通过在链的开头添加覆盖配置字典，可以优先使用覆盖配置，而不影响默认配置。
#   多个命令行参数：在处理命令行参数时，可能有多个来源，如命令行选项、环境变量、配置文件等。可以使用 ChainMap 将这些参数组合在一起，并按照优先级顺序进行查找。
#   嵌套字典的访问：当需要从多个嵌套字典中访问或修改值时，可以使用 ChainMap 来简化操作。通过将这些嵌套字典组合成一个 ChainMap，可以像访问单个字典一样进行操作。
'''

# 创建 ChainMap 对象
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain_map = ChainMap(dict1, dict2)

# 访问键值对
print(chain_map['a'])
# 输出：1
print(chain_map['b'])
# 输出：2
print(chain_map['c'])
# 输出：4


# 修改值
chain_map['b'] = 5
print(chain_map.maps)
# 输出：[{'a': 1, 'b': 5}, {'b': 3, 'c': 4}]


chain_map.maps[1]['b'] = 0
print(chain_map.maps)
# 输出：[{'a': 1, 'b': 5}, {'b': 0, 'c': 4}]


# 添加新的映射对象
dict3 = {'b': 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map['b'])
# 输出：6


# 获取所有映射对象，返回列表
print(new_chain_map.maps)
# 输出：[{'b': 6}, {'a': 1, 'b': 5}, {'b': 0, 'c': 4}]


for k, v in new_chain_map.items():
    print(k, v)

