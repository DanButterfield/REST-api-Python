from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of video is required", required=True)  # same thing as nullable
video_put_args.add_argument("likes", type=int, help="Likes on video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of video is required", required=True)

videos = {}


def abort_if_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video ID is not valid . . .")

def abort_if_video_exist(video_id):
    if video_id not in videos:
        abort(409, message="Video already Exists . . .")


class Video(Resource):
    def get(self, video_id):
        abort_if_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_id_doesnt_exist()
        del videos[video_id]
        return '',204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

# 200 means ok
# 201 means created
