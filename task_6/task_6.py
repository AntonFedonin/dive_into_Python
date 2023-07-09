# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

def digit_check():
    try:
        lenght = int(input('Введите год:\n'))
        return lenght
    except ValueError:
        print('Это должно быть число!\n')
        digit_check()


def find_year():
    year = digit_check()
    if year <= 1918 and year % 4 == 0:
        print(year, " год высокосный")
    elif year > 1918 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, " год высокосный")
    else:
        print(year, " год не высокосный")


find_year()

while True:
    key = input('Попробуем ещё разок? [y/n]: ')
    if key == 'y':
        find_year()
    else:
        print('Пока пока!')
        break
