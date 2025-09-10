# pip install intervaltree
import pickle
import time

from intervaltree import IntervalTree

import ipaddress


tree = IntervalTree()


# ip 转化为 数值类型
def ip_to_int(ip_str: str):
    if not ip_str:
        return 0
    return int(ipaddress.ip_address(ip_str))


# 数值类型 转化为 ip
def int_to_ip(ip_int: int):
    return ipaddress.ip_address(ip_int)


# 加载 ip库的 起始ip 转化为 IntervalTree 结构数据
def import_ip_lib(data: iter):
    for i, row in enumerate(data):
        if i == 0:
            continue
        sip = row[0]
        eip = row[1]
        area = row[2]
    tree.addi(ip_to_int(sip), ip_to_int(eip) + 1, area)


# 持久化 ip 库的 IntervalTree 结构数据
def save():
    with open("intervaltree.pkl", "wb") as f:
        pickle.dump(tree, f)


# 加载 ip 库的 IntervalTree 结构数据
def load():
    global tree
    with open("intervaltree.pkl", "rb") as f:
        tree = pickle.load(f)
        return tree


# 从 ip 库的 IntervalTree 结构数据，解析 ip
def parse(ip_str: str):
    interval = tree.at(ip_to_int(ip_str))
    area = '未知'
    if interval:
        area = interval.pop().data
    return area


if __name__ == '__main__':

    # start_time = time.time()
    # data = [(0, 1, '未知'),
    #         (2, 3, '404')]
    # import_ip_lib(data)
    # print(f'IP库导入IP数：{len(tree)}')
    # print(f'IP库导入耗时: {time.time() - start_time}')

    # start_time = time.time()
    # save()
    # print(f'IP持久化耗时: {time.time() - start_time}')

    start_time = time.time()
    tree = load()
    print(f'IP库加载的IP数：{len(tree)}')
    print(f'加载耗时: {time.time() - start_time}')

    # 解析ip
    print(parse("183.193.26.33"))
    print(parse("2a03:f80:852:151:236:20:7a:0"))
