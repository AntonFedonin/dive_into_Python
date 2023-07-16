# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def get_dict(**kwargs):
    res_dict = dict({})
    for key, value in kwargs.items():
        res_dict[key] = value
    return res_dict


result = get_dict(a=5, n=5.23, text="Превед медвед", l=[1, 2, 3], d={4: "hello", 5: "world", 6: "python"})
print(result)
