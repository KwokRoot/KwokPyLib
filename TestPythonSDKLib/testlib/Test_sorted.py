# list.sort() 排序
A = [('一', 1), ('三', 3), ('二', 2)]
A.sort(key=lambda x: x[1])
print(A)


# sorted() 排序

# 语法：sorted(iterable[, key][, reverse])
# 参数：
# iterable 可迭代对象，- sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator
# key （可选），function that serves as a key for the sort comparison
# reverse 反向（可选），If true, the sorted list is reversed (or sorted in Descending order)
# 返回值：a sorted list 一个排好序的列表
B = sorted(A, key=lambda x: x[1], reverse=True)
print(B)
print(type(B))

