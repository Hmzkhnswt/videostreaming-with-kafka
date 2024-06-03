from confluent_kafka import Consumer, KafkaError
import pickle

class KafkaVideoConsumer:
    def __init__(self, topic, group_id='video_group', bootstrap_servers='localhost:9092'):
        self.topic = topic
        self.consumer = Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        })

    def consume_frame(self):
        self.consumer.subscribe([self.topic])
        msg = self.consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                return None
            else:
                print(msg.error())
                return None
        
        frame = pickle.loads(msg.value())
        return frame

    def close(self):
        self.consumer.close()
