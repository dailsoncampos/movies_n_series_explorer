import requests

class Request:
    def __init__(self, url, setup_instance):
        self.response = requests.get(url, headers=setup_instance.get_headers())

    def get_response(self):
        return self.response