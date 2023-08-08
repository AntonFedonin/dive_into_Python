# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle
from pathlib import Path


def get_size(directory):
    size = 0
    for dir_path, dir_name, file_name in os.walk(directory):
        for name in dir_name:
            path = os.path.join(dir_path, name)
            size += os.path.getsize(path)
    return size


def get_collection(path):
    data = []
    for dir_path, dir_name, file_name in os.walk(path):
        for name in dir_name:
            little_path = os.path.join(dir_path, name)
            size = get_size(little_path)
            data.append({
                'name': name,
                'type': 'directory',
                'parent_directory': dir_path,
                'size': size
            })
        for name in file_name:
            filepath=os.path.join(dir_path, name)
            size=os.path.getsize(filepath)
            data.append({
                'name': name,
                'type': 'file',
                'parent_directory': dir_path,
                'size': size
            })
    with (open('directory_data.json','w') as json_file,
          open('directory_data.csv','w', newline='') as csv_file,
          open('directory_data.pickle','w') as pickle_file,):
        json.dump(data, json_file, indent=2)

        filenames = ['name', 'type', 'parent_directory', 'size']
        writer = csv.DictWriter(csv_file, filenames=filenames)
        writer.writeheader()
        writer.writerow(data)

        pickle.dump(data, pickle_file)



get_collection(Path.cwd())
