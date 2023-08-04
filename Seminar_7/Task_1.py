# Напишите функцию группового переименования файлов. Она должна:

#   принимать параметр желаемое конечное имя файлов.
#   При переименовании в конце имени добавляется порядковый номер.

#   принимать параметр количество цифр в порядковом номере.

#   принимать параметр расширение исходного файла.
#   Переименование должно работать только для этих файлов внутри каталога.

#   принимать параметр расширение конечного файла.

#   принимать диапазон сохраняемого оригинального имени.
#   Например для диапазона [3, 6] берутся буквы с 3 по 6
#   из исходного имени файла. К ним прибавляется желаемое
#   конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


def group_rename(name, numbers, start_ext, end_ext, count=None):

    files = [f.split(start_ext)[0] for f in os.listdir('.')
             if os.path.isfile(f) and f.endswith(start_ext)]

    if not files:
        print("Таких файлов нет")
        return

    for i, file in enumerate(files, 1):
        if count:
            start, end = count
            old_name = file[start - 1:end]

        new_name = old_name + name + f"{i:0{numbers}}" + end_ext

        os.rename(f'{file}{start_ext}', new_name)
        print(f"{file} переименован в {new_name}")


group_rename("Test_file_too", 4, ".docx", ".txt", count=[3, 6])