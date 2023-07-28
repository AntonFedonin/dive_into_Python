# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import re


def get_split_path(path):
    dir, full_name = path.rsplit('/', 1)
    name, ext = full_name.rsplit('.', 1)

    return dir, name, ext


input_path = '/dive_into_Python/Seminar_5/Task_2.py'

directory, name, extantion = get_split_path(input_path)
print("Путь: ", {directory}, "Имя: ", {name}, "Расширение: ", {extantion})
