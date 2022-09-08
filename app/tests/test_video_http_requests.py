"""
unit tests for Video class containing http request methods. ** Flask server must be running for tests to pass
"""
import requests
import unittest

LOCAL_HOST = "http://127.0.0.1:5000/"


class TestVideo(unittest.TestCase):

    def test_put(self):
        """ Testing put request to check requests.json() returns correct json object """

        should_return = {'id': 5, 'name': 'temp_video', 'views': 100, 'likes': 10}
        response = requests.put(LOCAL_HOST + "video/5", {"name": "temp_video", "likes": 10, "views": 100})
        under_test = response.json()

        self.assertEqual(should_return, under_test)

    def test_get(self):
        """ Testing get request to check the correct video json file is returned """

        should_return = {'id': 5, 'name': 'temp_video', 'views': 100, 'likes': 10}
        response = requests.get(LOCAL_HOST + "video/5")
        under_test = response.json()

        self.assertEqual(should_return, under_test)

    def test_video_does_not_exist(self):
        """ Testing the abort functionality if user gives video id that does not exist """

        should_return = {'message': 'Video id provided does not exist.'}
        response = requests.get(LOCAL_HOST + "video/100")
        under_test = response.json()

        self.assertEqual(should_return, under_test)
        self.assertEqual(404, response.status_code)

    def test_patch(self):
        """ Testing the update method to ensure videos are updated according to user edits """

        should_return = {"id": 5, "name": "temp_video", "views": 200, "likes": 250}
        response = requests.patch(LOCAL_HOST + "video/5", {"views": 200, "likes": 250})
        under_test = response.json()

        self.assertEqual(should_return, under_test)
        self.assertEqual(200, response.status_code)

    def test_delete(self):
        """ Testing the delete method to ensure video is deleted correctly given video id """

        should_return = 204
        response = requests.delete(LOCAL_HOST + "video/5")

        self.assertEqual(should_return, response.status_code)
