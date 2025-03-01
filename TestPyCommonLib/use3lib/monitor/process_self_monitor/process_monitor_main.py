import time

from ProcessMonitor import ProcessMonitor

if __name__ == '__main__':
    processMonitor = ProcessMonitor()
    processMonitor.start()

    # 业务代码逻辑
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(3)

