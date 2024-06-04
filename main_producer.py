from controller.producer_controller import ProducerController

if __name__ == "__main__":
    url = 'your_youtube_live_stream_url'
    topic = 'video_frames'
    producer_controller = ProducerController(url, topic)
    producer_controller.start_streaming()
