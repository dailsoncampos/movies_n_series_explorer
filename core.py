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
        response = Request(search_instance, setup_instance).get_response()
        Presenter(response)

core_instance = Core()
core_instance.call()
