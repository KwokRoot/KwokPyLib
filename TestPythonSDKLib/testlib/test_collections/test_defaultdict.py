import sys
from collections import defaultdict

'''
# defaultdict 可以设置一个默认值作为字典新 key 的默认值。该默认值可以是任何对象，包括函数、列表、元组、集合等。简化代码提高代码的可读性，而且可以防止 KeyError 异常的出现。
# defaultdict 重写了字典的__missing__方法。当访问字典中不存在的 key 时，__missing__方法负责返回默认值。因此，defaultdict 通过继承 dict，重载了__missing__方法，以提供默认值。
'''

d1 = {}
try:
    d1['name'].append("java")
except KeyError as e:
    print(e, file=sys.stdout)

d2 = defaultdict(list)
d2['name'].append("java")
d2['name'].append("python")

# 虽然 default_factory 是 list，但是它并不限制 defaultdict 中键的类型，可以添加任何类型的键和值
d2['worker'] = "DevOps"

# data_dic中还没有 age 这个键，那么default_factory就会自动生成一个空列表作为该键的值
print(d2['age'])


word_count1 = {}
word_list = ['a', 'b', 'c', 'b', 'b']
for word in word_list:
    if word not in word_count1:
        word_count1[word] = 1
    else:
        word_count1[word] += 1
print(word_count1)

word_count2 = defaultdict(int)
for word in word_list:
    # word_count2.setdefault(word, 0)
    word_count2[word] += 1
print(word_count2)


def init_dict():
    return {
        "name": "",
        "age": 18
    }


default_dict = defaultdict(init_dict)
print(default_dict["Kwok"])
default_dict["Kwok"]["name"] = "Kwok"
print(default_dict["Kwok"])

