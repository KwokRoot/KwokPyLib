# pip install intervaltree
from intervaltree import IntervalTree, Interval

# 初始化区间树
tree = IntervalTree([
    Interval(0, 60, "D"),
    Interval(60, 80, "C"),
    Interval(90, 100, "A")
])
print(tree.items())

# 动态添加区间
tree.add(Interval(80, 90, "B"))
tree.addi(95, 100, "S")
tree.append(Interval(85, 90, "B++"))
print(tree.items())


print("*" * 36)

# 判断数值是否在区间内
print(tree.at(75))
print(tree[96])

# 判断区间是否重叠，返回 bool
print(tree.overlaps(90, 95))
# 判断区间是否重叠，返回间隔
print(tree.overlap(90, 95))

for i in tree[98]:
    print(f'{i.begin}-{i.end}: {i.data}')


print("*" * 36)

# 删除间隔，Interval 必须和添加的间隔对象的 begin、end、data一致。
# remove 与 discard 区别：`remove()` 不存在该间隔，会抛异常。`discard()` 不抛异常。
interval_to_remove = Interval(85, 90, "B++")
# tree.remove(interval_to_remove)
tree.discard(interval_to_remove)

# 在此间隔的 Interval 才删除。
# tree.remove_envelop(95, 97)

# 包含此间隔的 Interval 都会删除。
# tree.remove_overlap(95, 97)

# 删除此间隔的 Interval，修改原间隔段
# tree.chop(95, 98)


print(tree.items())

print("*" * 36)

tree.print_structure()
print(tree)
print(tree.all_intervals)
print(tree.items())
print(tree.span())
print(tree.range())
print(tree.begin())
print(tree.end())


print("*" * 36)

tree2 = IntervalTree([
    Interval(85, 90, "up")
])

# 区间树交集
print(tree.intersection(tree2))
# 区间树差集
print(tree.difference(tree2))
# 区间树并集
print(tree.union(tree2))

# 区间树合并到两外一个区间树
tree.update(tree2)
print(tree)


print("*" * 36)

tree.clear()
print(tree)

