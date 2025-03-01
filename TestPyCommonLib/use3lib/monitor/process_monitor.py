import socket
import threading
import time


def start_monitor(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        print(f"监控端口 {port} 已开启")
        while True:
            client, addr = s.accept()
            client.send("up".encode("utf-8"))  # 可替换为实际监控数据
            client.close()


if __name__ == '__main__':
    monitor_thread = threading.Thread(target=start_monitor, args=(11110,))
    monitor_thread.start()
    print("监控端口已开启")

    # 业务代码逻辑
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(3)

