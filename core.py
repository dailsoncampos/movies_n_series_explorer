from setup import Setup
from search import Search
from request import Request
from presenter import Presenter

class Core:
    def __init__(self):
        self.setup_instance = Setup()
        self.search_instance = Search()

    def fetch_and_present(self, search_method, content_type):
        url = search_method()
        response = Request(url, self.setup_instance).get_response()

        if response.status_code == 200:
            data = response.json()
            print(f"\nLista de {content_type}s")
            Presenter.present(data, content_type)
        else:
            print(f"Erro {response.status_code}: Não foi possível obter os dados de {content_type}s.")

    def call(self):
        self.fetch_and_present(self.search_instance.for_movie, "filme")
        self.fetch_and_present(self.search_instance.for_tv_series, "série")

core_instance = Core()
core_instance.call()
