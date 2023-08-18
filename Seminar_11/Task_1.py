# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

import numpy as np


class Matrix:

    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        return f'{self.arr}'

    def __eq__(self, other):
        return self.arr is other.arr

    def sum (self, other):
        result = [map(sum, zip(*i)) for i in zip(self.arr, other.arr)]
        return result


a = np.array(Matrix([[1, 2, 3], [4, 5, 6]]))
# b = np.array(Matrix([[9, 8, 7], [6, 5, 4]]))
b = np.array(Matrix([[1, 2, 3], [4, 5, 6]]))


print(a)
print(b)

