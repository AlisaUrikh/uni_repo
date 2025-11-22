import tempfile
import os

def setup_bot_environment(configs):
    """Создает временные конфигурационные файлы для бота"""
    with tempfile.TemporaryDirectory() as temp_dir:
        config_path = os.path.join(temp_dir, "config.json")
        tokens_path = os.path.join(temp_dir, "tokens.json")
        webhook_path = os.path.join(temp_dir, "webhook.txt")

        open(config_path, 'w', encoding='utf-8').close()
        open(tokens_path, 'w', encoding='utf-8').close()
        open(webhook_path, 'w', encoding='utf-8').close()

        print(f"Пример 1 - Временная директория: {temp_dir}")
        print(f"Созданные файлы: {os.listdir(temp_dir)}")

def process_user_media(user_id, media_data):
    """Обрабатывает временные медиа-файлы пользователя"""
    with tempfile.TemporaryDirectory() as temp_dir:
        user_dir = os.path.join(temp_dir, str(user_id))
        os.makedirs(user_dir, exist_ok=True)

        avatar_path = os.path.join(user_dir, "avatar.jpg")
        with open(avatar_path, "w", encoding="utf-8") as f:
            f.write(media_data[0]) 

        for idx, media in enumerate(media_data[1:], 1):
            media_path = os.path.join(user_dir, f"media_{idx}.jpg")
            with open(media_path, "w", encoding="utf-8") as f:
                f.write(media)
                
        print(f"Пример 2 - Обработка медиа для пользователя {user_id}")
        print("Созданные файлы:", os.listdir(user_dir))

def cache_bot_data(cache_data):
    """Создает временный кэш данных бота"""
    with tempfile.TemporaryDirectory() as temp_dir:
        users_cache = os.path.join(temp_dir, "users_cache.json")
        messages_cache = os.path.join(temp_dir, "messages_cache.json")
        state_cache = os.path.join(temp_dir, "state_cache.json")

        open(users_cache, 'w', encoding='utf-8').close()
        open(messages_cache, 'w', encoding='utf-8').close()
        open(state_cache, 'w', encoding='utf-8').close()

        print("Пример 3 - Кэширование данных бота")
        print("Кэш-файлы:", os.listdir(temp_dir))

def create_temporary_logs(log_entries):
    """Создает временные лог-файлы для отладки"""
    with tempfile.TemporaryDirectory() as temp_dir:
        debug_log = os.path.join(temp_dir, "debug.log")
        errors_log = os.path.join(temp_dir, "errors.log")
        actions_log = os.path.join(temp_dir, "actions.log")

        with open(debug_log, "w", encoding="utf-8") as f:
            f.writelines(i + "\n" for i in log_entries if i.startswith("DEBUG:"))
        with open(errors_log, "w", encoding="utf-8") as f:
            f.writelines(i + "\n" for i in log_entries if i.startswith("ERROR:"))
        with open(actions_log, "w", encoding="utf-8") as f:
            f.writelines(i + "\n" for i in log_entries if i.startswith("ACTION:"))

        total_lines = 0
        for log_file in [debug_log, errors_log, actions_log]:
            with open(log_file, "r", encoding="utf-8") as f:
                total_lines += sum(1 for _ in f)

        print("Пример 4 - Временные логи для отладки")
        print(f"Общее количество записей в логах: {total_lines}")

if __name__ == "__main__":
    bot_configs = {
        "main": {"token": "abc123", "webhook": "https://bot.com"},
        "tokens": {"api_token": "tok123"}
    }
    setup_bot_environment(bot_configs)

    media_data = ["avatar_data", "photo_1", "photo_2"]
    process_user_media(12345, media_data)

    cache_data = {
        "users": {"user1": "active", "user2": "inactive"},
        "messages": ["msg1", "msg2", "msg3"],
        "state": {"bot_state": "running"}
    }
    cache_bot_data(cache_data)

    logs = [
        "DEBUG: Bot started",
        "ERROR: Connection failed", 
        "ACTION: User clicked button"
    ]
    create_temporary_logs(logs)
