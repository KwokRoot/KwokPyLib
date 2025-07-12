import time

import redis

r = redis.Redis.from_url("redis://:123456@127.0.0.1:6379/1", encoding="UTF-8", decode_responses=True)
print(str.format("连接状态: {}", r.ping()))

# ## 方式一：
# ## 注：`monitor()` 必须使用 with 开启资源管理，Monitor 对象 在 `__enter__` 中发送 `MONITOR` 命令。
with r.monitor() as m:
    for command_info in m.listen():
        t = command_info["time"]
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
        db = command_info["db"]
        client_address = command_info["client_address"]
        client_port = command_info["client_port"]
        client_type = command_info["client_type"]
        command = command_info["command"]
        print(f'{ts}, {client_address} -> db:{db}: {command}')


# ## 方式二：
# conn = r.connection_pool.get_connection('monitor')
# conn.send_command('MONITOR')
# response = conn.read_response()
# print("响应:", response)
# # 返回'OK'
#
# # 读取数据
# try:
#     while True:
#         response = conn.read_response()
#         print(response)
# except KeyboardInterrupt:
#     pass
# finally:
#     r.connection_pool.release(conn)

