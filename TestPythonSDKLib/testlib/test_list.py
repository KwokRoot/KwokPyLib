ls = [2, 4, 6, 8, 10]

for i, l in enumerate(ls):
    print("%s -> %s" % (i, l))
    print(f"{i} -> {l}")


print("*" * 36)


# 集合推导式
print([x for x in ls if x % 4 == 0])

print(list(x - 1 for x in ls))

