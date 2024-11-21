class Search:
    def __init__(self):
        self.title = input("Pesquisar por: ")
    
    def for_movie(self):
        return f"https://api.themoviedb.org/3/search/movie?query={self.title}"

    def for_tv_series(self):
        return f"https://api.themoviedb.org/3/search/tv?query={self.title}"
