def decode_to_dec(num, base, hex_dict):
    start_num = num  # наше начальное число
    outstring = ''   # строка с решением, которую будем выводить
    num_in_dec = 0   # инициируем наше число
    for i in range(len(str(num))):  # основной цикл программы
        last_digit = num[-1].upper() # отрезаем последнюю цифру
        outstring += str(hex_dict[last_digit]) + "*" + str(base) + "^" + str(i) + ' '
        # добавляем в выходную строку действия, нужные для вычисления
        if i != len(str(start_num)) - 1: # добавляем + между всеми слагаемыми
            outstring += "+ "
        num_in_dec += hex_dict[last_digit]*base**i # производим вычисления с отрезанной цифрой
        num = num[:-1]        # отбрасываем последнюю цифру
    return "Считаем так:", outstring, "Результат в десятичной системе:", num_in_dec


def highest_exponent(num, base):
    exp = 0
    while True:
        if base ** exp < num < base ** (exp + 1):
            return exp
        exp += 1

def encode_from_dec(num, base, reversed_dict):  #
    num = int(num)
    num_encoded = ''
    exp = highest_exponent(num, base)
    while exp != -1:
        count = 0
        while num >= base ** exp:
            num -= base ** exp
            count += 1
        num_encoded += reversed_dict[count]
        exp -= 1
    return f"Ваше число в {base}-ичной системе:", num_encoded



hex_dict = {"0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
    }  # Словарь цифра:число

reversed_dict = {0: '0',
                 1: '1',
                 2: '2',
                 3: '3',
                 4: '4',
                 5: '5',
                 6: '6',
                 7: '7',
                 8: '8',
                 9: '9',
                 10: 'A',
                 11: 'B',
                 12: 'C',
                 13: 'D',
                 14: 'E',
                 15: 'F'
    }  #словарь число: цифра

def decoding():
    num = input("Введите число в вашей системе счисления: \n")    #ввод числа
    base = int(input("Введите основание, по которому будем считать: \n")) #ввод основания
    print(*decode_to_dec(num, base, hex_dict), sep='\n')   # вывод ответа


def encoding():
    num = input("Введите число в десятичной системе счисления: \n")    #ввод числа
    base = int(input("Введите основание, по которому будем кодировать: \n")) #ввод основания
    print(*encode_from_dec(num, base, reversed_dict), sep='\n')   # вывод ответа


def main_prog():
    print('Вас приветствует ФорМарин 2.0 \nНу что ж, начнём?')  # приветствие
    while True:
        user_string = input("Введите DC, чтобы перевести число из другой системы счисления в 10-ную.\nВведите EC, чтобы перевести ваше число из 10-ной в другую систему счисления.\n").upper()
        if user_string == 'DC':
            decoding()
            while True:  # спросить пользователя о дальнейших действиях
                user_input = input("Посчитать ещё одно число? (Y/N)\n").lower()
                if user_input == 'y':
                    break
                elif user_input == 'n':
                    quit(0)
                else:
                    print("Некорректный ввод, введите Y/N\n")
        elif user_string == 'EC':
            encoding()
            while True:  # спросить пользователя о дальнейших действиях
                user_input = input("Посчитать ещё одно число? (Y/N)\n").lower()
                if user_input == 'y':
                    break
                elif user_input == 'n':
                    quit(0)
                else:
                    print("Некорректный ввод, введите Y/N\n")
        else:
            print("Некорректный ввод")
            continue


main_prog()
