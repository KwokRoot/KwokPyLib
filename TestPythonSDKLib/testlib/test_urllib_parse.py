# url 编码解码
from urllib import parse

# 编码
print(parse.quote('http://10.1.188.110:9090/api/v1/query?query=kminion_kafka_broker_info{job="Kafka-jq-01"}&time=1666804596'))
# 解码
print(parse.unquote('http%3A//10.1.188.110%3A9090/api/v1/query%3Fquery%3Dkminion_kafka_broker_info%7Bjob%3D%22Kafka-jq-01%22%7D%26time%3D1666804596'))


print("*" * 36)


# 转换路径参数
data = {
    "index": 1,
    "size": 10
}
print(parse.urlencode(data))


