import yaml

class Setup:
    def __init__(self):
        with open('credentials.yml', 'r') as file:
            credentials = yaml.safe_load(file)

        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + credentials['api_token']
        }

    def get_headers(self):
        return self.headers
