from datetime import date
from loader_2 import TextDataLoader

loader = TextDataLoader()
posts = loader.extract_posts()
cleaned_posts = loader.clean_text(posts)

"""
Перепишите тесты для методов clean_text и extract_posts используя:

- Assert с сообщениями об ошибках (2 любых теста)
- Множественные проверки в одном assert (2 любых теста)
- Создайте кастомную функцию, которая проверяет 2 теста сразу
"""

"""Задание 1"""
assert len(posts)>0, "Список постов не должен быть пустым"
assert all(cleaned_post['text'].islower() for cleaned_post in cleaned_posts), "В тексте постов не должно быть заглавных букв"

"""Задание 2"""
assert all('text' in post for post in posts) and all('date' for post in posts), "Ключи 'date' и 'text' обязательно должны быть в словаре"
assert all('!' not in cleaned_post['text'] for cleaned_post in cleaned_posts) and all('?' not in cleaned_post['text'] for cleaned_post in cleaned_posts), "После обработки должны быть удалены все '!' и '?'"

"""Задание 3"""
def assert_text_extracted_and_cleaned():
    """Кастомная функция проверки очистки текста"""
    loader = TextDataLoader()
    posts = loader.extract_posts()
    cleaned_posts = loader.clean_text(posts)
    d = date.today().strftime("%Y-%m-%d")
    assert all(post['date'][:10]<d in post for post in posts), "Даты публикации постов должны быть раньше сегодняшней"
    assert all('/n' not in cleaned_post['text'] for cleaned_post in cleaned_posts), "В очищенном тексте не должно быть переносов строк"

assert_text_extracted_and_cleaned()
