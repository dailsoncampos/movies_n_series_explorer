class Search:
    BASE_URL = "https://api.themoviedb.org/3/search"

    def __init__(self):
        self.title = self.get_title()

    def get_title(self):
        title = input("Pesquisar por: ").strip()
        if not title:
            raise ValueError("O título não pode ser vazio!")
        return title

    def generate_url(self, type_):
        return f"{self.BASE_URL}/{type_}?query={self.title}"

    def for_movie(self):
        return self.generate_url("movie")

    def for_tv_series(self):
        return self.generate_url("tv")