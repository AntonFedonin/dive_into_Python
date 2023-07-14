# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

mult_1 = 2
mult_2 = 2
count = 0
while mult_1 < 10:
    while mult_2 < 11:
        prod = mult_1 * mult_2
        print(mult_1, " x ", mult_2, " = ", prod)
        mult_2 += 1
    mult_1 += 1
    mult_2 = 2
