# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

number = int(input("Введите целое число: "))


def to_hex(num) -> str:
    hex_digits = '0123456789ABCDEF'
    result = ''
    while num > 0:
        remainder = num % 16
        hex_digit = hex_digits[remainder]
        result = hex_digit + result
        num //= 16
    return result


print("\n",to_hex(number))

print("\n", hex(number))
