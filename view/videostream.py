from vidgear.gears import CamGear

class VideoStream:
    def __init__(self, source):
        self.stream = CamGear(source=source, stream_mode=True, logging=True).start()

    def read_frame(self):
        frame = self.stream.read()
        if frame is None:
            return None
        return frame

    def stop(self):
        self.stream.stop()
