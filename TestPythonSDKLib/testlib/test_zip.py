a = ['a', 'b', 'c', 'd']
b = ['1', '2', '3']
c = ['一', '二', '三', '四', '五']

# 当多个序列中元素个数不一致时，会以最短的序列为准进行压缩。
# Python3 中 zip() 函数返回 zip 对象，Python2 中 zip() 函数直接返回列表。
z = zip(a, b, c)
print(type(z))
print(z)
zl = list(z)
print(zl)


# zip() 函数在 Python3 中，只能遍历一次，遍历一次后，内存就会释放！！！(Python2中可以访问多次).
z2 = zip(a, b, c)

print(f'{"*" * 3} 第一次变遍历 {"*" * 3}')
for zi in z2:
    print(zi)

print(f'{"*" * 3} 第二次变遍历 {"*" * 3}')
for zi in z2:
    print(zi)


print(f'{"*" * 3} 一次压缩，解包 {"*" * 3}')
z3 = zip(a, b, c)
a3, b3, c3 = z3
print(a3)
print(b3)
print(c3)

print(f'{"*" * 3} 二次压缩，解包 {"*" * 3}')
a2, b2, c2 = zip(*zip(a, b, c))
print(a2)
print(b2)
print(c2)


print(f'{"*" * 3} 使用 zip() 函数，字典 K、V 互转 {"*" * 3}')

d = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
}
d2 = dict(zip(d.values(), d.keys()))
print(d2)

