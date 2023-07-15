# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [9, "Hello", 3, 88, 9, "Hello", 3, 88]
new_list = []

for i in my_list:
    if my_list.count(i) > 1 and i not in new_list:
        new_list.append(i)

print(my_list, '\n', new_list)
