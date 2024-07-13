# pip install expiringdict
from expiringdict import ExpiringDict
import dill as dill
import time

# # expiringdict 是可设置自动过期时间，固定长度 dict 拓展类型的类库。


cache = ExpiringDict(max_len=1, max_age_seconds=3)
cache["k1"] = "v1"
cache["k2"] = "v2"
print(cache.get("k1"))
print(cache.get("k2"))


# 注：根据源码，如果 items 是 ExpiringDict 实例，当 max_len/max_age_seconds = None，则取 items 的 max_len/max_age_seconds。
cache2 = ExpiringDict(max_len=None, max_age_seconds=8, items=cache)

# print(cache2)
# cache2["k3"] = "v3"

print(cache2)
time.sleep(5)
print(cache.get("k2"))
print(cache2.get("k2"))


# 使用 `dill` 类库持久化
pickled_cache = dill.dumps(cache2)
cache3 = dill.loads(pickled_cache)
print(cache3.get("k2"))
time.sleep(2)
print(cache3.get("k2"))
time.sleep(1)
print(cache3.get("k2"))

