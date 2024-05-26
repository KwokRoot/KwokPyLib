# pip install deepdiff
from deepdiff import DeepDiff, DeepSearch, grep, extract, DeepHash

d1 = {
    "a": 3,
    "b": "2",
    "c": 3
}

d2 = {
    "a": 1,
    "b": 2,
    "d": 6
}


# DeepDiff() 深度对比对象差异
df = DeepDiff(d1, d2, ignore_order=True)
print(df)


# DeepSearch() 根据值或者键名查找对象路径
ds = DeepSearch(d1, "b", case_sensitive=False)
print(ds)

# grep() 根据值或者键名查找对象路径
dg = d1 | grep("b")
print(dg)


# extract() 根据键路径获取值，路径以 `root` 开始
path = "root['b']"
print(extract(d1, path))


# DeepHash() 对对象的键、值进行哈希处理
dh = DeepHash(d1)
print(dh)

