from glob import glob
import mimetypes
from flask import  Flask, Response,make_response,render_template,flash
from flask_restful import Api, Resource
from Utils.camera import Stream 
from Utils.camera import Camera as cm
from Utils.camera2 import Video as vd
from Utils.form import TestForm
import os

app = Flask(__name__,static_folder="static")
api = Api(app)

app.secret_key = "my super secret key" #for the form

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
        self.file = None
        self.form = TestForm()
        return make_response(render_template("test.html",file=self.file,form=self.form))

    def post(self):
        self.file = None
        self.form = TestForm()
        index = 0
        if self.form.validate_on_submit():
            self.file = self.form.file.data
            search_path = "static/archive/"
            for root,folders,files in os.walk(search_path):
                for file in files:
                    if self.file == file:
                        my_list = root.split("/")
                        name = my_list[len(my_list)-1]
                        name = name.replace("__"," ")
                        name = name.replace("_"," ")
                        path = "../" + root + "/" + file
                                

                index += 1
                    
        self.form.file.data = None
        return make_response(render_template("test.html",file=self.file,form=self.form,name=name,path=path))

api.add_resource(Index, "/")
api.add_resource(Test, "/test/")
api.add_resource(Camera, "/camera/")
api.add_resource(Video, "/video/")


if __name__ == "__main__":
    app.run(debug=True)