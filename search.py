class Search:
    def __init__(self):
        search_for = input("Pesquisar por: ")
        self.url = self.generate_url(search_for)

    def generate_url(self, title):
        url = "https://api.themoviedb.org/3/search/movie?query=" + title
        return url
