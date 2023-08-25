from collections import OrderedDict

# OrderedDict 是 Python test_collections 模块中的有序字典，它可以按照元素添加的顺序来存储键值对，保证了元素的顺序性。
# 注：Python2 中 dict 默认是无序的。Python3.6 +，dict 类型变为有序对象集合。

ordered_dict = OrderedDict()
ordered_dict['java'] = 1
ordered_dict['python'] = 2
ordered_dict['go'] = 3
ordered_dict['php'] = 4
ordered_dict['nodejs'] = 5

for k, v in ordered_dict.items():
    print(k, v)


print(ordered_dict.popitem())
print(ordered_dict.popitem(last=False))

# 将元素移动到 OrderedDict 的末尾
ordered_dict.move_to_end('go')
print(ordered_dict)

# 将元素移动到 OrderedDict 的头部
ordered_dict.move_to_end('go', last=False)
print(ordered_dict)


print("*" * 36)


# OrderedDict 实现先进先出的 FIFO 队列
class FIFO(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        if len(self) >= self.capacity:
            self.popitem(last=False)
        super().__setitem__(key, value)


q = FIFO(3)
q['a'] = 1
q['b'] = 2
q['c'] = 3
print(q)
q['d'] = 4
print(q)

