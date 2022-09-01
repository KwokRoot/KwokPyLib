import time


# pip install kafka-python
from kafka import KafkaProducer

kafka_hosts = "127.0.0.1:9092"
# username = "admin"
# password = "admin-pwd"


producer = KafkaProducer(
    bootstrap_servers=kafka_hosts,
    # sasl_mechanism="PLAIN",
    # security_protocol='SASL_PLAINTEXT',
    # sasl_plain_username=username,
    # sasl_plain_password=password,
)

i = 0
while True:
    i += 1
    data = {
        "id": i
    }
    result = producer.send("test", str.encode(str(data), "utf-8"))
    producer.flush()
    print(result.succeeded())
    time.sleep(1)

