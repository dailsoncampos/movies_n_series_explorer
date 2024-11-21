from setup import Setup
from search import Search
from request import Request
from presenter import Presenter

class Core:
    def __init__(self):
        pass

    def call(self):
        setup_instance = Setup()
        search_instance = Search()

        movie_url = search_instance.for_movie()
        movies_response = Request(movie_url, setup_instance).get_response()

        tv_series_url = search_instance.for_tv_series()
        tv_series_response = Request(tv_series_url, setup_instance).get_response()

        Presenter(movies_response, tv_series_response)

core_instance = Core()
core_instance.call()
