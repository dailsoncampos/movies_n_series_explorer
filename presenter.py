class Presenter:
    def __init__(self, movie_content, tv_series_content):
        if movie_content.status_code == 200 and tv_series_content.status_code:
            movie_data = movie_content.json()
            tv_series_data = tv_series_content.json()

            print("Lista de filmes")
            self.movies_list(movie_data)

            print("Lista de séries")
            self.tv_series_list(tv_series_data)

        else:
            print(f"Erro {movie_content.status_code}: Não foi possível obter os dados.")
            print(f"Erro {tv_series_content.status_code}: Não foi possível obter os dados.")

    def movies_list(self, data):
        movies = [{'title': movie['original_title'], 'overview': movie['overview']} for movie in data['results']]

        for item in movies:
            print(f"\nTitle: {item['title']}\nOverview: {item['overview']}")

    def tv_series_list(self, data):
        tv_series = [{'title': movie['original_name'], 'overview': movie['overview']} for movie in data['results']]

        for item in tv_series:
            print(f"\nTitle: {item['title']}\nOverview: {item['overview']}")