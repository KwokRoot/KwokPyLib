# pip install kafka-python
from kafka import KafkaConsumer, TopicPartition


kafka_hosts = "127.0.0.1:9092"
# username = "admin"
# password = "admin-pwd"


consumer = KafkaConsumer(
    bootstrap_servers=kafka_hosts,
    group_id="kafka_test",
    # sasl_mechanism="PLAIN",
    # security_protocol='SASL_PLAINTEXT',
    # sasl_plain_username=username,
    # sasl_plain_password=password,
)

print("连接状态：{}".format(consumer.bootstrap_connected()))

topic = "test"
timestamps = 1661930391000

partitions = consumer.partitions_for_topic(topic)

topic_partition = []
for p in partitions:
    topic_partition.append(TopicPartition(topic, p))

consumer.assign(topic_partition)


## 将 offset 偏移到某个时间点
partition_info = {}
for p in topic_partition:
    partition_info[p] = timestamps
# print(partition_info)

topic_partition_offset = consumer.offsets_for_times(partition_info)
# print(topic_partition_offset.get(topic_partition[0]))

if topic_partition_offset.get(topic_partition[0]):
    for i in topic_partition:
        # print(topic_partition_offset.get(i)[0])
        consumer.seek(i, topic_partition_offset.get(i)[0])

    consumer.commit()
else:
    print("该时间点后没日志，请检查时间戳...")


# ## 将 offset 偏移到起始位置消费
# topic_partition_offset = consumer.beginning_offsets(topic_partition)
#
# for i in topic_partition:
#     # print(topic_partition_offset.get(i)[0])
#     consumer.seek(i, topic_partition_offset.get(i))
#
# consumer.commit()


## 将 offset 偏移到结束位置消费
# topic_partition_offset = consumer.end_offsets(topic_partition)
#
# for i in topic_partition:
#     # print(topic_partition_offset.get(i)[0])
#     consumer.seek(i, topic_partition_offset.get(i))
#
# consumer.commit()


# ！！！注：直接将 offset 偏移到开始/结束位置，只在 consumer.poll() 消费前起作用，手动偏移不能使用！需要使用以上方式！！！
# consumer.seek_to_beginning()
# consumer.seek_to_end()


