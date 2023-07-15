import input
import functions as f

remainter = 0  # Остаток средств на счёте
counter = 1  # Счётчик операций
MULTIPLICITY = 50  # Кратность снятия или пополнения
LOW_DEFAULT = 30  # Минимальный размер комисии
HIGH_DEFAULT = 600  # Максимальный размер комисии
TAKE_OF_PROCENT = 0.015  # Процент за снятие 1,5
AFTER_3_OPERATION_PROCENT = 0.03  # Процент комиссии после трёх операций
WEALTH_TAX = 0.1  # 10% налог на богатство с каждой операции при остатке больше 5 000 000
KING_OF_MONEY = 5_000_000  # сумма на остатке после которой взымается налог на богатство


def menu(rem, count):
    greetings = 'Здравствуйте, клиент!'
    choice = 'Выберите операцию:'
    take_off = '1. Снять'
    top_up = '2. Пополнить'
    ex = '3. Выйти'
    print(f'{greetings} Ваш остаток {rem} у.е.\n\n{choice}\n\n{take_off}\n\n{top_up}\n\n{ex}')
    number = input.digit_check()
    choice_rival(number, rem, count)


def choice_rival(num, rem, count):
    if num == 1:
        rem = f.take_off(rem, count)
        count += 1
        if rem > KING_OF_MONEY:
            rem = f.take_wealth_tax(rem)
            menu(rem, count)
        else:
            menu(rem, count)
    elif num == 2:
        rem = f.top_up(rem, count)
        count += 1
        if rem > KING_OF_MONEY:
            rem = f.take_wealth_tax(rem)
            menu(rem, count)
        else:
            menu(rem, count)
    elif num == 3:
        shutdown()
    else:
        print("Выбран не существующий пункт меню. Попробуйте ещё раз.")
        menu(rem, count)


def shutdown():
    print("Спасибо что воспользовались услугами нашего банка! До свидания!")
    exit()


menu(remainter, counter)
