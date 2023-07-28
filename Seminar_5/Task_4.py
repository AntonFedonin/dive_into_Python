# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def get_fibonacci_nums(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


input_num = int(input("Введите число: "))
result_list = list(get_fibonacci_nums(input_num))
print(result_list)
