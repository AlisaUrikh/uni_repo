import argparse
import os
import sys

def find_files_by_extension(path, extensions):
    for root, dirs, files in os.walk(path):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension[1:].lower() in [ext.lower() for ext in extensions]:
                print(os.path.join(root, file))

def main():
    parser = argparse.ArgumentParser(description='Поиск файлов по расширению')
    parser.add_argument('path', help='Путь для поиска')
    parser.add_argument('--ext', nargs='+', required=True, help='Расширения файлов')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print(f"Ошибка: путь '{args.path}' не существует")
        sys.exit(1)
    
    find_files_by_extension(args.path, args.ext)

if __name__ == "__main__":
    main()


# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/finder.py /Users/alisa/Desktop/uni_repo/argparse --ext py 
# /Users/alisa/Desktop/uni_repo/argparse/finder.py
# /Users/alisa/Desktop/uni_repo/argparse/create_password.py
# /Users/alisa/Desktop/uni_repo/argparse/word_count.py
