import os
import json
import re
import pandas as pd

class TextDataLoader:
    def __init__(self):
        self.path = '/Users/alisa/Desktop/uni_repo/d/result.json'
        self.posts_data = self.extract_posts()

    def _validate_file_path(self, path):
        """Валидация файла."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Путь '{path}' не найден!")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"'{path}' является директорией, а не файлом!")
        if not path.endswith('.json'):
            raise ValueError(f"Файл не является корректным JSON")

    def load_data(self, path=None):
        """Загрузка файла."""
        if path is None:
            path = self.path
        self._validate_file_path(path)
        try:
            with open(path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
            return json_data
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    def extract_posts(self, json_data=None):
        """Извлечение постов из файла."""
        if json_data is None:
            json_data = self.load_data(self.path)
        messages = json_data.get('messages', [])
        posts = []
        for message in messages:
            full_text = ''
            text = message.get('text')
            if isinstance(text, str):
                full_text += text
            elif isinstance(text, list):
                for elem in text:
                    if isinstance(elem, str):
                        full_text += elem
                    else:
                        full_text += elem['text']
            if full_text.strip():
                posts.append({
                    'id': message.get('id'),
                    'text': full_text,
                    'date': message.get('date')
                })
    
        return posts


    def clean_text(self, posts_data=None):
        """Обработка постов."""
        if posts_data is None:
            posts = self.posts_data
        else:
            posts = posts_data
        
        for post in posts:
            cleaned_text = re.sub(r'[\s\n\t]+', ' ', post['text'])
            cleaned_text = re.sub(r'[^\w\s]', ' ', cleaned_text)
            cleaned_text = cleaned_text.strip().lower()
            post['text'] = cleaned_text
        return posts
    
    def save_to_csv(self, cleaned_posts, output_path='output.csv'):
        """Сохранение результата в CSV."""
        df = pd.DataFrame(cleaned_posts)
        df.to_csv(output_path, index=False)

     

loader = TextDataLoader()
posts = loader.extract_posts()
cleaned_posts = loader.clean_text(posts)
result = loader.save_to_csv(cleaned_posts)

#1. Дополнить класс так, чтобы он мог выгружать информацию по id телеграм-канала с использованием api (например, telethon)
