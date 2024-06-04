from controller.consumer_controller import ConsumerController

if __name__ == "__main__":
    topic = 'video_frames'
    consumer_controller = ConsumerController(topic)
    consumer_controller.start_displaying()
