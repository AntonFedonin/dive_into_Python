# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

def dict_generator(names, rates, prem):
    result_dict = {name: rate * float(premia.rstrip("%")) / 100
                   for name, rate, premia in zip(names, rates, prem)}
    return result_dict


list_names = ["Алексей", "Елена", "Кристина", "Егор"]
list_rates = [10000, 45000, 38450, 94334]
list_prem = ["10.25", "17.30", "7.15", "55.10"]

dict = dict_generator(list_names, list_rates, list_prem)
print(dict)
