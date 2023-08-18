# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:

    def __init__(self, arr1, arr2=None):
        self.arr1 = arr1
        if arr2 is None:
            self.arr2 = arr1
        else:
            self.arr2 = arr2

    def _str(self):
        return f'{self.arr1}, {self.arr2}'




