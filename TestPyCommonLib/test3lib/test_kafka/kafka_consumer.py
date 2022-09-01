import time

# pip install kafka-python
from kafka import KafkaConsumer, TopicPartition

kafka_hosts = "127.0.0.1:9092"
# username = "admin"
# password = "admin-pwd"


consumer = KafkaConsumer(
    bootstrap_servers=kafka_hosts,
    group_id="kafka_test",
    # auto_offset_reset='latest',
    # enable_auto_commit=False,
    # sasl_mechanism="PLAIN",
    # security_protocol='SASL_PLAINTEXT',
    # sasl_plain_username=username,
    # sasl_plain_password=password,
)

print("连接状态：{}".format(consumer.bootstrap_connected()))

topic = "test"

partitions = consumer.partitions_for_topic(topic)

topic_partition = []
for p in partitions:
    topic_partition.append(TopicPartition(topic, p))

consumer.assign(topic_partition)
# consumer.seek_to_beginning()

while True:
    for rs in consumer.poll().values():
        for r in rs:
            log = str(r.value, "utf-8")
            print(log)
    time.sleep(1)


