import socket
from threading import Thread


class ProcessMonitor (Thread):

    def __init__(self, monitor_port=11110):
        super(ProcessMonitor, self).__init__()
        self.monitor_port = monitor_port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', self.monitor_port))
            s.listen()
            print(f"port: {self.monitor_port} is start.")
            while True:
                client, addr = s.accept()
                client.send("up".encode("utf-8"))
                client.close()

