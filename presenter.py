class Presenter:
    @staticmethod
    def present(data, content_type):
        items = [{'title': item.get('original_title') or item.get('original_name'), 'overview': item['overview']}
                 for item in data.get('results', [])]

        for item in items:
            print(f"\nTítulo ({content_type}): {item['title']}\nResumo: {item['overview']}")
