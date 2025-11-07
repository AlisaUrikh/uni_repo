from loader_2 import TextDataLoader

def test_clean_text_with_assert():
    """Тестирование clean_text с использованием assert"""
    loader = TextDataLoader()
    
    # Тест очистки пробелов
    result = loader.clean_text([{"text": "  Hello  World  "}])
    assert result[0]['text'] == "hello world", "Должны удаляться лишние пробелы"
    
    # Тест нижнего регистра
    result = loader.clean_text([{"text": "HELLO"}])
    assert result[0]['text'] == "hello", "Текст должен быть в нижнем регистре"
    
    # Тест специальных символов
    result = loader.clean_text([{'text': "Hello! @user #tag"}])
    assert "!" not in result[0]['text'], "Должны удаляться специальные символы"
    assert "@" not in result[0]['text'], "Должны удаляться @ символы"

    result = loader.clean_text([{'text': "Hello, user!?.:; #tag"}])
    assert "?" not in result[0]['text'], "Должны удаляться '?'"
    assert "," not in result[0]['text'], "Должны удаляться ','"
    assert "." not in result[0]['text'], "Должны удаляться '.'"
    assert ";" not in result[0]['text'], "Должны удаляться ';'"
    assert ":" not in result[0]['text'], "Должны удаляться ':'"
    assert "!" not in result[0]['text'], "Должны удаляться '!'"
    assert "#" not in result[0]['text'], "Должны удаляться '#'"

    result = loader.clean_text([{'text': ""}])
    assert "" == result[0]['text'], "Пустые строки не должны обрабатываться"

    

test_clean_text_with_assert()
