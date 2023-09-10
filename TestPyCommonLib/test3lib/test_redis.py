import redis

# # redis 连接池
# redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password="123456", db=0, decode_responses=True)
# redis_pool = redis.ConnectionPool.from_url("redis://:123456@127.0.0.1:6379/0", encoding="UTF-8", decode_responses=True)
# r = redis.Redis(connection_pool=redis_pool)

r = redis.Redis(host="127.0.0.1", port=6379, password="123456", db=0, decode_responses=True)
# r = redis.Redis.from_url("redis://:123456@127.0.0.1:6379/0", encoding="UTF-8", decode_responses=True)

print("Pong: " + str(r.ping()))

for i in range(6):
    r.set("key" + "-" + str(i), i)

r.set("中文键", "中文值")

print(sorted(r.keys()))

# r.flushdb(0)
r.close()

