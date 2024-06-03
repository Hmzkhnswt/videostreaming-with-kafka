from model.kafka_producer import KafkaVideoProducer
from view.videostream import VideoStream

class ProducerController:
    def __init__(self, source, topic):
        self.video_stream = VideoStream(source)
        self.kafka_producer = KafkaVideoProducer(topic)

    def start_streaming(self):
        while True:
            frame = self.video_stream.read_frame()
            if frame is None:
                break
            self.kafka_producer.produce_frame(frame)
        self.kafka_producer.flush()
        self.video_stream.stop()
