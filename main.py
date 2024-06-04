import argparse
from controller.producer_controller import ProducerController
from controller.consumer_controller import ConsumerController

def main():
    parser = argparse.ArgumentParser(description="Kafka Video Streaming Pipeline")
    parser.add_argument('mode', choices=['produce', 'consume'], help="Mode to run the script in: 'produce' to send frames to Kafka, 'consume' to receive and display frames from Kafka")
    parser.add_argument('--url', type=str, help="URL of the YouTube live stream (required for produce mode)")
    parser.add_argument('--topic', type=str, default='video_frames', help="Kafka topic to produce/consume video frames")
    args = parser.parse_args()

    if args.mode == 'produce':
        if not args.url:
            print("URL of the YouTube live stream is required in produce mode")
            return
        producer_controller = ProducerController(args.url, args.topic)
        producer_controller.start_streaming()
    elif args.mode == 'consume':
        consumer_controller = ConsumerController(args.topic)
        consumer_controller.start_displaying()

if __name__ == "__main__":
    main()
