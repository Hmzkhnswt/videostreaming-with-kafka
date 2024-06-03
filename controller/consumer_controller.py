from model.kafka_consumer import KafkaVideoConsumer
from view.videodisplay import VideoDisplay

class ConsumerController:
    def __init__(self, topic):
        self.kafka_consumer = KafkaVideoConsumer(topic)
        self.video_display = VideoDisplay()

    def start_displaying(self):
        while True:
            frame = self.kafka_consumer.consume_frame()
            if frame is None:
                continue
            if not self.video_display.show_frame(frame):
                break
        self.kafka_consumer.close()
        self.video_display.close()
