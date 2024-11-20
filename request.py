import requests

class Request:
    def __init__(self, search_instance, setup_instance):
        self.response = requests.get(search_instance.url, headers=setup_instance.get_headers())

    def get_response(self):
        return self.response