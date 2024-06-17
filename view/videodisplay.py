import cv2
import os
import time
import yt_dlp
from dotenv import load_dotenv

# Load environment variables from .env.dev file
load_dotenv(dotenv_path='../.env.dev')
youtube_url = os.getenv('YOUTUBE_URL')

if not youtube_url:
    raise ValueError("No YOUTUBE_URL found in environment variables")

class VideoDisplay:
    def __init__(self, storing_dir="Frames"):
        self.storing_dir = storing_dir
        os.makedirs(self.storing_dir, exist_ok=True)
        self.frame_counter = 0

    def saving_frames(self, source=youtube_url):
        self.source = source
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.source, download=False)
            video_url = info_dict.get("url", None)
            
        if not video_url:
            raise ValueError("Failed to extract video URL")
        
        stream = cv2.VideoCapture(video_url)
        while True:
            ret, frame = stream.read()
            if not ret:
                break
            cv2.imwrite(f"{self.storing_dir}/frame_{self.frame_counter}.jpg", frame)
            self.frame_counter += 1
            time.sleep(1)  # Wait for 1 second to achieve 1 FPS
        stream.release()

