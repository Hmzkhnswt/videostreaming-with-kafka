import cv2
import yt_dlp
 
url = 'https://www.youtube.com/watch?v=O3DPVlynUM0'
 
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
}
 
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    video_url = info_dict.get("url", None)
 
cap = cv2.VideoCapture(video_url)
 
while True:
    ret, frame = cap.read()
    if not ret:
        break
   
    cv2.imshow('This is the YTDLP_Frame', frame)
   
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()