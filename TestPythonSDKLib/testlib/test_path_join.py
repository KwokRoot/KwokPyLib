import os
from pathlib import Path


def path_join_01(file_path: str = None):
    if file_path:
        dir_path = os.path.dirname(file_path)
    else:
        dir_path_curr = os.path.dirname(__file__)
        file_path = os.path.join(dir_path_curr, "logs", "log1.txt")
        dir_path = os.path.dirname(file_path)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def path_join_02(file_path: str = None):
    if file_path:
        file_path = Path(file_path)
    else:
        file_path = Path(Path.cwd(), "logs", "log2.txt")

    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch(exist_ok=True)


if __name__ == '__main__':
    file_path = "/opt/devops/logs/log1.txt"
    path_join_01(file_path)

    path_join_01()

    file_path = "/opt/devops/logs/log2.txt"
    path_join_02(file_path)

    path_join_02()

