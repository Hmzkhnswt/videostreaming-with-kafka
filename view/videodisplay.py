import cv2
import os

class VideoDisplay:
    
    def __init__(self, storing_dir="Frames"):
        self.storing_dir = storing_dir
        os.makedirs(self.storing_dir, exist_ok=True)
        self.frame_counter = 0
    
    def show_frame(self, frame):
        cv2.imshow("Frame", frame)
        
        # Save the frame
        frame_path = os.path.join(self.storing_dir, f"frame{self.frame_counter}.jpg")
        cv2.imwrite(frame_path, frame)
        self.frame_counter += 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True

    def close(self):
        cv2.destroyAllWindows()
