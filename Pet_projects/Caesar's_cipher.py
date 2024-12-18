eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"




def is_correct_direction():
    direction = input("Вы хотите шифровать или дешифровать?\n")

    if direction in ['шифровать', 'дешифровать', 'Шифровать', 'Дешифровать']:
        return direction
    else:
        print('Что-то неправильно! Введите шифровать или дешифровать')

is_correct_direction()
