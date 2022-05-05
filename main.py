import mimetypes
from flask import  Flask, Response,make_response,render_template
from flask_restful import Api, Resource
from Utils.camera import Stream 
from Utils.camera import Camera as cm
from Utils.camera2 import Video as vd

app = Flask(__name__,static_folder="static")
api = Api(app)


class Index(Resource):
    def get(self):
        return make_response(render_template("index.html"))

class Camera(Resource):
    def get(self):
        stream = Video()
        my_stream = stream.get()
        return make_response(render_template("camera.html"))
    def video(self):
        return Response(gen(vd()),
        mimetype = 'multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + 
        b'\r\n\r\n'
        )

class Video(Resource):
    def __init__(self):
        self.stream = Stream()
        
    def get(self):
        cam = cm()
        return Response(cam.gen_video(self.stream),
        mimetype = 'multipart/x-mixed-replace; boundary=frame'
        )

class Test(Resource):
    def get(self):
        return make_response(render_template("test.html"))
    def post(self,my_form):
        return make_response(render_template("test.html"))



api.add_resource(Index, "/")
api.add_resource(Test, "/test/")
api.add_resource(Camera, "/camera/")
api.add_resource(Video, "/video/")


if __name__ == "__main__":
    app.run(debug=True)