""" model.py - contains VideoModel (SQL table) for storing video info """
from .database import db


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"
