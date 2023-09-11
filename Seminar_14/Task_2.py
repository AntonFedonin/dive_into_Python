# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте
# Если возможно в один из вариантов ниже
# - целое положительное число
# - вещественное положительное или отрицательное число
# - строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# - строку

import doctest

def trans_data(data):
    """
    This function transforms input data
    :param data:
    data(str): input data
    :return:
    int, float, str: Transformed data
    """
    # >>> trans_data("42")
    # 42
    # >>> trans_data("3.14")
    # 3.14

    if data.isdecimal():
        result = int(data)
    elif data.replace('.', '', 1).isdecimal():
        result = float(data)
    elif data[0] == "-" and data.replace('-', '', 1).replace('.', '', 1).isdecimal():
        result = float(data)
    elif data != data.lower():
        result = data.lower()
    else:
        result = data.upper()

    return result


data = input('Введите данные: ')
result = trans_data(data)
print(f'{result = }')
