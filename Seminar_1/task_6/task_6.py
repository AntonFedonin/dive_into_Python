# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

def digit_check():
    try:
        input_num = int(input('Введите год:\n'))
        return input_num
    except ValueError:
        print('Это должно быть число!\n')
        digit_check()


def find_year():
    year = digit_check()
    print(type(year))
    gregorian_calendar = 1582
    if year <= gregorian_calendar and year % 4 == 0:
        result = "Год высокосный"
    elif year > gregorian_calendar and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result = "Год высокосный"
    else:
        result = "Год не высокосный"
    print(year, result)



find_year()


while True:

    key = input('Попробуем ещё разок? [y/n]: ')
    if key == 'y':
        find_year()
    else:
        print('Пока пока!')
        break
