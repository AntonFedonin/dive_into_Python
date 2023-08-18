# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

from copy import deepcopy
import random


class Matrix:

    def __init__(self, arr):
        self.matrix = deepcopy(arr)

    def __repr__(self):
        return f'{self.matrix}'

    def __eq__(self, other):
        return self.matrix is other.matrix

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        matrix = result
        return Matrix(matrix)


def get_array() -> list[list[int]]:
    new = list()

    for i in range(0, 2):
        temp = []
        for j in range(0, 3):
            temp.append(random.randint(0, 9))
        new.append(temp)
    return new


a = Matrix(get_array())
b = Matrix(get_array())
print(a)
print(b)
c = a + b
print(c)
