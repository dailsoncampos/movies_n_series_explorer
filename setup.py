import yaml

class Setup:
    def __init__(self, credentials_file='credentials.yml'):
        self.headers = self.load_credentials(credentials_file)

    @staticmethod
    def load_credentials(file_path):
        try:
            with open(file_path, 'r') as file:
                credentials = yaml.safe_load(file)
                return {
                    "accept": "application/json",
                    "Authorization": f"Bearer {credentials['api_token']}"
                }
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo de credenciais não encontrado.")
        except KeyError:
            raise KeyError("Token de API não encontrado nas credenciais.")
        except Exception as e:
            raise Exception(f"Erro ao carregar as credenciais: {e}")

    def get_headers(self):
        return self.headers
