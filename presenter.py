class Presenter:
    def __init__(self, content):
        if content.status_code == 200:
            print(content.text)
        else:
            print(f"Erro {content.status_code}: Não foi possível obter os dados.")