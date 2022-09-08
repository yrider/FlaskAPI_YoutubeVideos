""" video.py - contains video class for HTTP request methods for REST API interaction """
from flask_restful import Resource, reqparse, abort, fields, marshal_with
from .model import VideoModel
from .database import db


# automatically parse through requests being sent to ensure we get correct data from user
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="We require a name for your video", required=True)
video_put_args.add_argument("views", type=int, help="We require the number of views for your video", required=True)
video_put_args.add_argument("likes", type=int, help="We require the number of likes for your video", required=True)

# used for patching/updating a video currently saved in database. Not all inputs required.
video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="We require a name for your video")
video_patch_args.add_argument("views", type=int, help="We require the number of views for your video")
video_patch_args.add_argument("likes", type=int, help="We require the number of likes for your video")

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


def _video_exists(video_id: str) -> bool:
    """ check if video exists """
    result = VideoModel.query.filter_by(id=video_id).first()
    return result is not None


class Video(Resource):

    # marshal_with returns query back into json format based on resource field var. e.g., {id: id, name: name ...}
    @staticmethod
    @marshal_with(resource_fields)
    def get(video_id: str) -> dict:
        """ get a json file containing video information given a video_id """
        if _video_exists(video_id):
            return VideoModel.query.filter_by(id=video_id).first()
        abort(http_status_code=404, message="Video id provided does not exist.")  # 404 status code = does not exist

    @staticmethod
    @marshal_with(resource_fields)
    def put(video_id: str) -> dict:
        """ create a new video given a video id and following video info: name, views and likes """
        if not _video_exists(video_id):
            args = video_put_args.parse_args()
            video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
            # add video and commit new row to database
            db.session.add(video)
            db.session.commit()
            return video, 201  # 201 code = video created
        abort(http_status_code=409, message="Video id already exists.")  # 409 status code = already exists

    @staticmethod
    @marshal_with(resource_fields)
    def patch(video_id: str) -> dict:
        if _video_exists(video_id):
            args = video_patch_args.parse_args()
            result = VideoModel.query.filter_by(id=video_id).first()
            if args['name']:
                result.name = args["name"]
            if args['views']:
                result.views = args["views"]
            if args['likes']:
                result.likes = args["likes"]
            db.session.commit()
            return result, 200  # 200 status code = resource updated successfully
        abort(http_status_code=404, message="Video id provided does not exist.")  # 404 status code = does not exist

    @staticmethod
    @marshal_with(resource_fields)
    def delete(video_id: str):
        """ delete a video given a video id """
        if _video_exists(video_id):
            result = VideoModel.query.filter_by(id=video_id).first()
            db.session.delete(result)
            db.session.commit()

            return "", 204  # 204 status code = deleted successfully
        abort(http_status_code=404, message="Video id provided does not exist.")
