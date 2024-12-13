import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cntPw = int(input('Укажите количество паролей для генерации:\n'))
lenPw = int(input('Укажите длину одного пароля:\n'))
digOn = input('Включать ли цифры 0123456789? (y/n)\n')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)\n')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)\n')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)\n')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)\n')

if digOn == 'y':
    chars += digits
if ABCon == 'y':
    chars += uppercase_letters
if abcOn == 'y':
    chars += lowercase_letters
if chOn == 'y':
    chars += punctuation
if excOn == 'y':
    for el in  'il1Lo0O':
        chars.replace(el, '')

def generate_passwort(lenPw, chars):
    password = ''
    for i in range(lenPw):
        password += random.choice(chars)
    return password

print('Вот список, который у меня получился:')

for j in range(cntPw):
    print(generate_passwort(lenPw, chars))

