import requests

class Request:
    def __init__(self, url, setup_instance):
        self.url = url
        self.headers = setup_instance.get_headers()

    def get_response(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição para {self.url}: {e}")
            return None