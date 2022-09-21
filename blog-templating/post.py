import requests

url = "https://api.npoint.io/c790b4d5cab58020d391"


class Post:
    def __init__(self):
        self.all_blogs = []
        self.get_blog()

    def get_blog(self):
        response = requests.get(url)
        self.all_blogs = response.json()
        return self.all_blogs
