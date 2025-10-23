import argparse
import string
import random

def generate_password(length, use_uppercase, use_digits, use_symbols):
    charset = string.ascii_lowercase
    
    if use_uppercase:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation
    password = ''.join(random.choice(charset) for i in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Генератор паролей с настройками")
    parser.add_argument('-l', '--length', type=int, default=12, help="Длина пароля")
    parser.add_argument('--uppercase', action='store_true', help="Добавить заглавные буквы")
    parser.add_argument('--digits', action='store_true', help="Добавить цифры")
    parser.add_argument('--symbols', action='store_true', help="Добавить другие символы")
    
    args = parser.parse_args()
    
    password = generate_password(args.length, args.uppercase, args.digits, args.symbols)
    print("Сгенерированный пароль:", password)

if __name__ == "__main__":
    main()


# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/create_password.py --length 12
# Сгенерированный пароль: kpdbpqkvqvco
# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/create_password.py -l 16 --uppercase --digits --symbols
# Сгенерированный пароль: T>XXg=ipu=px;6,0
