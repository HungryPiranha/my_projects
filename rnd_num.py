import random
from math import log, ceil

print('Добро пожаловать в числовую угадайку')

def max_tries_count(right_bound):
    res = ceil(log(right_bound, 2))
    return res


def is_valid(input_data, right_bound):
    if input_data.isdigit() == True:
        input_data = int(input_data)
        if 1 <= input_data <= right_bound:
            return True
        else:
            return False
    else:
        return False

def guess_game(rnd_num, right_bound):
    count = 0
    while True:
        input_data = input()
        if is_valid(input_data, right_bound) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        count += 1
        if int(input_data) < rnd_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif int(input_data) > rnd_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
    return count


while True:
    print("Новая игра! Введите правую границу диапазона значений:", end = '\n')
    right_bound = int(input())
    rnd_num = random.randrange(1, right_bound + 1)
    print('Первая попытка! GL & HF.')
    count = guess_game(rnd_num, right_bound)
    print(f'Ваше число попыток: {count}', '\n', f'Число попыток, необходимое для нахождения числа бинарным делением: {max_tries_count(right_bound)}')
    print("Сыграем ещё разок? (Y/N)")
    while True:
        next_game = input()
        if next_game == "N":
            quit('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        elif next_game == "Y":
            break
        else:
            print("Введены неверные данные. Y - да, N - нет")
