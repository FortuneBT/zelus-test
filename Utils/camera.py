import cv2

class Stream(object):
    def __init__(self):
        self.stream = cv2.VideoCapture(0)
    
    def __del__(self):
        self.stream.release()
    
    def get_frame(self):
        ret,image = self.stream.read()
        ret,jpeg = cv2.imencode(".jpg",image)
        return jpeg.tobytes()

class Camera():
    def gen_video(self,stream:Stream):
        while True:
            frame = stream.get_frame()
            yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame +
            b'\r\n\r\n'
            )