from main.video import Video

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

# configure database
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.create_all()

# add Video class to api for http requests
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == '__main__':
    app.run(debug=True)
