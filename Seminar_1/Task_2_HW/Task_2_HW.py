# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на
# единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def digit_check():
    try:
        input_num = int(input('Введите число от 0 до 100000:\n'))
        return input_num
    except ValueError:
        print('Это должно быть число!\n')
        digit_check()


def chek_num(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число не является простым")


number = digit_check()
while number < 0 or number > 100000:
    number = digit_check()

chek_num(number)
