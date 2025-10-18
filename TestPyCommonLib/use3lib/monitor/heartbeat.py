import os
from datetime import datetime


def heartbeat(heartbeat_log: str = None):
    if heartbeat_log:
        file_path = os.path.dirname(heartbeat_log)
    else:
        dir_path_curr = os.path.dirname(__file__)
        heartbeat_log = os.path.join(dir_path_curr, "logs", "heartbeat_log")
        file_path = os.path.dirname(heartbeat_log)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    dts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(heartbeat_log, "a+", encoding="utf-8") as f:
        f.write(dts + "\n")


if __name__ == '__main__':

    heartbeat("/opt/devops/logs/heartbeat.log")

    # print(__file__)
    # heartbeat()

