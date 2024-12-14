from confluent_kafka import Producer
import json

def send_data_to_kafka(data: dict,
                       kafka_server: str = "localhost:9092",
                       topic: str = "github-commits"):
    """
    Отправка данных (коммитов) в топик Kafka
    """
    producer_config = {
        "bootstrap.servers": kafka_server
    }
    producer = Producer(producer_config)

    data_json = json.dumps(data)
    producer.produce(topic, value=data_json)
    producer.flush()