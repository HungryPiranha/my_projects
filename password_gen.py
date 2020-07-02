import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ''

def password_length_func():
    while True:
        password_length = input("Введите длину пароля: \n")
        if password_length.isdigit() == False:
            print("Неверные данные, введите число")
            continue
        else:
            password_length = int(password_length)
            return password_length

def using_digits_func(chars, digits):
     while True:
        using_digits = input("Использовать цифры в случайных паролях? (Y/N) \n").capitalize()
        if using_digits == "Y":
            chars += digits
            return chars
        elif using_digits == "N":
            return chars
            break
        else:
            print("Неверные данные. Y - да, N - нет")
            continue

def using_lowercase_func(chars, lowercase_letters):
     while True:
        using_lowercase= input("Использовать строчные буквы в случайных паролях? (Y/N) \n").capitalize()
        if using_lowercase == "Y":
            chars += lowercase_letters
            return chars
        elif using_lowercase == "N":
            return chars
            break
        else:
            print("Неверные данные. Y - да, N - нет")
            continue

def using_uppercase_func(chars, uppercase_letters):
     while True:
        using_uppercase = input("Использовать заглавные буквы в случайных паролях? (Y/N) \n").capitalize()
        if using_uppercase == "Y":
            chars += uppercase_letters
            return chars
        elif using_uppercase == "N":
            return chars
            break
        else:
            print("Неверные данные. Y - да, N - нет")
            continue

def using_punctuation_func(chars, punctuation):
     while True:
        using_punctuation = input("Использовать спецсимволы в случайных паролях? (Y/N) \n").capitalize()
        if using_punctuation == "Y":
            chars += punctuation
            return chars
        elif using_punctuation == "N":
            return chars
            break
        else:
            print("Неверные данные. Y - да, N - нет")
            continue

def using_controversial_symbols_func(chars):
    while True:
        using_controversial_symbols = input("Использовать в случайных паролях символы, которые легко перепутать с другими? (Y/N) \n").capitalize()
        if using_controversial_symbols == "Y":
            chars.replace('i', '')
            chars.replace('1', '')
            chars.replace('l', '')
            chars.replace('L', '')
            chars.replace('O', '')
            chars.replace('0', '')
            chars.replace('o', '')
            return chars
        elif using_controversial_symbols == "N":
            return chars
            break
        else:
            print("Неверные данные. Y - да, N - нет")
            continue

def generate_password(password_length, chars):
    password = ''
    for i in range(password_length):
        password += random.choice(chars)
    return password


while True:
    password_count = input("Добрый день, сколько случайных паролей понадобится? \n")
    if password_count.isdigit() == False:
        print("Неверные данные. Введите целое число")
        continue
    else:
        password_count = int(password_count)
    password_length = password_length_func()
    chars =using_digits_func(chars, digits)
    chars = using_lowercase_func(chars, lowercase_letters)
    chars =using_uppercase_func(chars, uppercase_letters)
    chars = using_punctuation_func(chars, punctuation)
    chars = using_controversial_symbols_func(chars)
    for i in range(password_count):
        print(generate_password(password_length, chars))
    while True:
        generate_again = input('Хотите ещё паролей? Их есть у меня (Y/N) \n').capitalize()
        if generate_again == 'Y':
            break
        elif generate_again == 'N':
            print('Спасибо за использование программы, до встречи!')
            quit(0)
        else:
            print("Неверные данные. Y - да, N - нет")
            continue

