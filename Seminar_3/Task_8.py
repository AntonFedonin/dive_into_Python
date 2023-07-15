# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

dict_friends = {"Степан": ("Палатка", "Спальник", "Фонарик"), "Коля": ("Спальник", "Спички", "Фонарик"),
                "Оля": ("Спальник", "Фонарик", "Продукты"), "Галя": ("Спальник", "Котелки", "Столовые приборы")}

all_staff_set = {}
unique_staff = {}
popular_staff = {}

for value in dict_friends.values():
        all_staff_set.add(value)
print(all_staff_set)
