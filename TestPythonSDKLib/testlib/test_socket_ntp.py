import socket
import struct
from datetime import datetime


NTP_SERVER = "ntp2.aliyun.com"
NTP_PORT = 123
# 1970-1900 seconds
TIME1970 = 2208988800

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b'\x1b' + 47 * b'\0'  # 参考 RFC 2030，构建一个 NTP 请求包
client.sendto(data, (NTP_SERVER, NTP_PORT))  # 123 是 NTP 协议默认的 UDP 端口
data, address = client.recvfrom(1024)  # 接收服务器响应

if data:
    response = struct.unpack("!12I", data)
    ntp_time = response[10]

    print('Response received from:', address)
    print(datetime.fromtimestamp(ntp_time - TIME1970))

