# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

import numpy as np


class Matrix:

    def __init__(self, arr):
        self.arr = arr

    def __repr__(self):
        return f'{self.arr}'

    def __eq__(self, other):
        return self.arr is other.arr

    def __add__(self, other):
        lst = []
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                lst.append(self.arr[i, j] + other.arr[i, j])
        arr = lst

        return Matrix(arr)


a = Matrix([[1, 2, 3], [4, 5, 6]])
# b = np.array(Matrix([[9, 8, 7], [6, 5, 4]]))
b = Matrix([[1, 2, 3], [4, 5, 6]])

c = a + b
print(a)
print(b)
print(c)
