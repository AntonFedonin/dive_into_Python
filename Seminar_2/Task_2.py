# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions

a = input('Введите первую дробь форматом a/b\n')
b = input('Введите вторую дробь форматом a/b\n')

numerator_1 = int(a.split('/')[0])
denominator_1 = int(a.split('/')[1])
numerator_2 = int(b.split('/')[0])
denominator_2 = int(b.split('/')[1])
f1 = fractions.Fraction(numerator_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)

sum = f1+f2
prod=f1*f2

print(f'\n {a} + {b} = {sum}\n {a} * {b} = {prod}')
