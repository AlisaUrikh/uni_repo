import argparse

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def count_lines(text):
    return text.count('\n') + 1 if text else 0

def main():
    parser = argparse.ArgumentParser(description="Подсчёт слов/символов/строк в файле")
    parser.add_argument('filename', help='Путь к файлу')
    parser.add_argument('--words', action='store_true', help='Подсчет количества слов')
    parser.add_argument('--chars', action='store_true', help='Подсчет количества символов')
    parser.add_argument('--lines', action='store_true', help='Подсчет количества строк')

    args = parser.parse_args()

    try:
        with open(args.filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    if args.words:
        print(f"Слова: {count_words(content)}")
    if args.chars:
        print(f"Символы: {count_chars(content)}")
    if args.lines:
        print(f"Строки: {count_lines(content)}")

if __name__ == '__main__':
    main()


#alisa@MacBook-Air-Alisa uni_repo % python3 argparse/word_count.py /Users/alisa/Desktop/uni_repo/argparse/text --words
# Слова: 297
# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/word_count.py /Users/alisa/Desktop/uni_repo/argparse/text --words --lines
# Слова: 297
# Строки: 6
# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/word_count.py /Users/alisa/Desktop/uni_repo/argparse/text --words --lines --chars
# Слова: 297
# Символы: 2046
# Строки: 6
