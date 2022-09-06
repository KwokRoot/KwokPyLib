import socket

# 查看当前主机名
print(f'当前主机名为: {socket.gethostname()}')

# 根据主机名称获取当前 IP
print(f'当前主机 IP 为: {socket.gethostbyname(socket.gethostname())}')


print("*" * 36)


# Mac 上述方法均返回 127.0.0.1
# 通过使用 socket.getaddrinfo() 函数获取真实的 IP
# 获取当前主机 IPV4 和 IPV6 的所有 IP 地址(所有系统均通用)
addrs = socket.getaddrinfo(socket.gethostname(), None)
for item in addrs:
    print(item)


print("*" * 18)

# 仅获取当前 IPV4 地址(最内层)
print('当前主机 IPV4 地址为(最内层): ' + [item[4][0] for item in addrs if ':' not in item[4][0]][-1])

# 仅获取当前 IPV4 地址(最外层)
ipv4 = ""
for item in addrs:
    if ':' not in item[4][0]:
        ipv4 = item[4][0]
        break
print('当前主机 IPV4 地址为(最外层): ' + ipv4)


print("*" * 36)


# 通过建立 socket 连接，获取当前 IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]
print('当前主机的 IP 为: ' + ip)

