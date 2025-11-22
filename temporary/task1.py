import tempfile
import json
import os
from time import time
import requests

def get_cached_weather_data(city, cache_minutes=10):
    """Получает данные о погоде с кэшированием в временный файл"""
    temp_dir = tempfile.gettempdir()
    cache_path = os.path.join(temp_dir, f"weather_{city}.json")
    
    if os.path.exists(cache_path):
        age = time() - os.path.getmtime(cache_path)
        if age < cache_minutes * 60:
            print(f"Используем кэш для {city}")
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
            
    API_KEY = ""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(weather_data, f)
        return weather_data
    except Exception as e:
        return {"error": f"Ошибка: {e}"}

def cleanup_weather_cache():
    """Очищает все кэш-файлы погоды"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_dir = os.path.dirname(temp_file.name)

    for file in os.listdir(temp_dir):
        if file.startswith("weather_") and file.endswith(".json"):
            os.unlink(os.path.join(temp_dir, file))
    
    print("Кэш очищен")

# Использование:
print(get_cached_weather_data("Moscow"))
print(get_cached_weather_data("Moscow"))  # Возьмет из кэша!
print(get_cached_weather_data("SPb"))
print(get_cached_weather_data("Saint Petersburg"))

# В конце можно почистить
cleanup_weather_cache()
