import itertools
import math

'''
排列: 指从给定个数的元素中取出指定个数的元素进行排序。
组合: 指从给定个数的元素中仅仅取出指定个数的元素，不考虑排序。
'''

# product 笛卡尔积(有放回抽样排列)
# 可迭代对象的笛卡尔积，相当于嵌套 for 循环
for i in itertools.product('ABC', repeat=2):
    print(i, end=", ")


print("\n" + "=" * 36)


# permutations 排列(不放回抽样排列)
for i in itertools.permutations('ABC', 2):
    print(i, end=", ")

# 排列计算(Python Version >= 3.8)
print("\n" + "-" * 9)
print(math.perm(3, 2))


print("\n" + "=" * 36)


# combinations 组合，没有重复(不放回抽样组合)
for i in itertools.combinations('ABC', 2):
    print(i, end=", ")

# 组合计算(Python Version >= 3.8)
print("\n" + "-" * 9)
print(math.comb(3, 2))


print("\n" + "=" * 36)


# combinations_with_replacement 组合，有重复(有放回抽样组合)
for i in itertools.combinations_with_replacement('ABC', 2):
    print(i, end=", ")


