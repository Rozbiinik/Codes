import random
print('Попробуйте угадать число, которое я загадал')

def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

print('Введите число от 1 до 100')

def is_valid_num():
    while True:
        s = input()
        if is_valid(s):
            return int(s)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def total():
    num = random.randint(1, 100)
    count = 0
    while True:
        n = is_valid_num()
        count += 1
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали, поздравляем! Ваше количество попыток: {count}')
            break

def question():
    while True:
        print(f'Хотите сыграть ещё раз? \nДа или Нет\n')
        answer = input()
        if answer == 'Да':
            print('Введите число от 1 до 100')
            total()
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        

total()
question()