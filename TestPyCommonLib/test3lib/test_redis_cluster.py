# pip install redis>=4.1.0
from redis.cluster import RedisCluster, ClusterNode

# iP + port 方式
rc = RedisCluster(host='10.10.110.101', port=6379, password="123456", decode_responses=True)
print(rc.get_nodes())


# Redis URL 方式
rc = RedisCluster.from_url("redis://:123456@10.10.110.101:6379/0", encoding="UTF-8", decode_responses=True)
print(rc.get_nodes())


# ClusterNode 方式
nodes = [
    ClusterNode("10.10.110.101", 6379),
    ClusterNode("10.10.110.102", 6379),
    ClusterNode("10.10.110.103", 6379),
    ClusterNode("10.10.110.104", 6379),
    ClusterNode("10.10.110.105", 6379),
    ClusterNode("10.10.110.106", 6379),
]

rc = RedisCluster(startup_nodes=nodes, password='123456', decode_responses=True)
print(rc.get_nodes())


print(len(rc.keys("*")))
print(len(rc.keys("*", target_nodes=RedisCluster.ALL_NODES)))
print(len(rc.keys("*", target_nodes=RedisCluster.PRIMARIES)))
print(len(rc.keys("*", target_nodes=RedisCluster.REPLICAS)))

