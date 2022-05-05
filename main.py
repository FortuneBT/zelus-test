from flask import  Flask,make_response,render_template
from flask_restful import Api, Resource

app = Flask(__name__,static_folder="static")
api = Api(app)


class Index(Resource):
    def get(self):
        return make_response(render_template("index.html"))


class Test(Resource):
    def get(self):
        return make_response(render_template("test.html"))



api.add_resource(Index, "/")
api.add_resource(Test, "/test/")


if __name__ == "__main__":
    app.run(debug=True)