""" terminal_test.py - used as visual guide in addition to unittests to check outputs are as expected """
import requests

LOCAL_HOST = "http://127.0.0.1:5000/"

# Create new video called API Video with id 1 and add to SQL db
response = requests.put(LOCAL_HOST + "video/1", {"name": "API Video", "likes": 10, "views": 100})
print(response.json())

input()

# Get request to check video has been successfully saved in db
response = requests.get(LOCAL_HOST + "video/1")
print(response.json())

input()

# Check get request is not working when user provides id that does not exist
response = requests.get(LOCAL_HOST + "video/6")
print(response.json())

input()

# Check patch/update request is working by changing likes from 10 to 100 for video with id = 1
response = requests.patch(LOCAL_HOST + "video/1", {"likes": 100})
print(response.json())

input()

# delete video and print response and status code (should be 204 for successful delete)
response = requests.delete(LOCAL_HOST + "video/1")
print(response)
print(response.status_code)