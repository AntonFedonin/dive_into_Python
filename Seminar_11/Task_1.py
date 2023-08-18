# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

from copy import deepcopy


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
        return Matrix(result)


# def get_array() -> list[list[int]]:
#     new = [[i for i in range(random.randrange(0, 9))] for i in range(random.randrange(0, 9))]
#     return new


a = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[1, 2, 3], [4, 5, 6]])
c = a + b

print(a)
print(b)
print(c)
