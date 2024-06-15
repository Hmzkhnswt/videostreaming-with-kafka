import cv2
import os
from vidgear.gears import CamGear
from dotenv import load_dotenv
from view.videostream import VideoStream

load_dotenv(dotenv_path = '../.env.dev')
youtube_url = os.getenv('YOUTUBE_URL')

class VideoDisplay:
    
    def __init__(self, storing_dir="Frames"):
        self.storing_dir = storing_dir
        os.makedirs(self.storing_dir, exist_ok=True)
        self.frame_counter = 0
        
    def SavingFrmaes(self):
        Stream = VideoStream(youtube_url)
        Frames = Stream.read_frame()
        while Frames is not None:
            self.frame_counter += 1
            cv2.imwrite(f"{self.storing_dir}/frame_{self.frame_counter}.jpg", Frames)

        
