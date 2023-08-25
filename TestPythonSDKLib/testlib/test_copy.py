import copy

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(f'{"*" * 9} 浅 copy 示例 {"*" * 9}')

# list2 = list1.copy()
list2 = copy.copy(list1)
print(id(list1), id(list2))

list1[1].remove(4)
print(list1)
print(list2)


print(f'{"*" * 9} 深 copy 示例 {"*" * 9}')

list3 = copy.deepcopy(list1)
print(id(list1), id(list3))

list2[1].remove(5)
print(list1)
print(list2)
print(list3)

