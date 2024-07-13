# pip install cacheout
from cacheout import Cache

import time

# # python 缓存库 cacheout


# 可以重写 on_get、on_set、on_delete 回调方法
def on_delete(key, value, cause):
    print(f'>>> {key}: {value} 被删除...')


cache = Cache(maxsize=1, ttl=3, timer=time.time, default=None, on_delete=on_delete)
cache.set('k1', 'v1')
cache.set('k2', 'v2', 5)
print(cache)
print(cache.get('k2'))
print(cache.get_ttl('k2'))

time.sleep(3)
print(cache.get_ttl('k2'))


print(cache.stats.info())
cache.configure(maxsize=10, ttl=10, enable_stats=True)
print(cache.get_ttl('k2'))

print(cache.stats.info())


print("*" * 36)


# 根据参数，缓存一个函数
@cache.memoize(ttl=5, typed=True)
def func(a, b):
    time.sleep(2)
    return a + b


print(time.strftime("1. %Y-%m-%d, %H:%M:%S", time.localtime()))

# 第一次执行，缓存函数及参数
func(1, 2)
print(time.strftime("2. %Y-%m-%d, %H:%M:%S", time.localtime()))

# 命中缓存
func(1, 2)
print(time.strftime("3. %Y-%m-%d, %H:%M:%S", time.localtime()))

# 非命中缓存(typed=True)
func(1, 2.0)
print(time.strftime("4. %Y-%m-%d, %H:%M:%S", time.localtime()))

# 不经过缓存，使用原始方法
func.uncached(1, 2)
print(time.strftime("5. %Y-%m-%d, %H:%M:%S", time.localtime()))

