import json

class Dataset:
    def __init__(self, filename='/content/api.json'):
        self.filename = filename
        self.data = self._read_json()

    def _read_json(self):
        """ Функция для чтения JSON-файла. """
        try:
            with open (self.filename, 'r', encoding= 'utf-8') as file:
                text = json.load(file)
                return(text)
        except FileNotFoundError:
            print (f'Ошибка: файл "{self.filename}" не найден!')
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON")
    
    def get_song(self, id):
        """ Функция для поиска песни по id. """
        if self.data is not None:
            for i in self.data:
                if i['id'] == id:
                    return i['title']
            return 'Нет записи с таким id'

    def find_similar(self, id):
        """Функция для поиска похожих песен."""
        songs = []
        if self.data is not None:
            for i in self.data:
                if i['id'] == id:
                    songs = [self.data[y-1]['title'] for y in i['similar_ids']]
            return songs
        return 'Нет записи с таким id'
        
        
if __name__ == '__main__':
    id = 4
    dataset = Dataset()
    result = dataset.get_song(id)
    similar_songs = dataset.find_similar(id)
    print(f'Найденная песня: {result}')
    print(f'Похожие песни: {', '.join(similar_songs)}')
