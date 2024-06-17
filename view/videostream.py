import yt_dlp
from dotenv import load_dotenv
import os
import cv2

load_dotenv(dotenv_path='../.env.dev')
youtube_url = os.getenv('YOUTUBE_URL')
# youtube_url = "https://www.youtube.com/watch?v=O3DPVlynUM0"

if not youtube_url:
    raise ValueError("No YOUTUBE_URL found in environment variables")

class VideoStream:
    def __init__(self, source):
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(source, download=False)
            video_url = info_dict.get("url", None)
        
        if not video_url:
            raise ValueError("Failed to extract video URL")

        # Initialize the video stream with OpenCV
        self.stream = cv2.VideoCapture(video_url)
        if not self.stream.isOpened():
            raise ValueError("Failed to open video stream")

    def read_frame(self):
        ret, frame = self.stream.read()
        if not ret:
            return None
        return frame

    def stop(self):
        self.stream.release()

# Initialize the VideoStream with the YouTube URL
stream = VideoStream(youtube_url)

# Display the video stream frames
while True:
    frame = stream.read_frame()
    if frame is None:
        break
    cv2.imshow('Live Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if __name__ == "__main__":
    stream.stop()
    cv2.destroyAllWindows()
