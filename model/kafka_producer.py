from confluent_kafka import Producer
import pickle

class KafkaVideoProducer:
    def __init__(self, topic, bootstrap_servers='localhost:9092'):
        self.topic = topic
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})

    def delivery_report(self, err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    def produce_frame(self, frame):
        data = pickle.dumps(frame)
        self.producer.produce(self.topic, data, callback=self.delivery_report)
        self.producer.poll(0)

    def flush(self):
        self.producer.flush()


# Path: model/kafka_consumer.py