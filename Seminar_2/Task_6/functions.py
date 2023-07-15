import input
import controller as cr



def top_up(rem, count):
    print('Укажите сумму для пополнения кратную 50:')
    cash = input.digit_check()
    if cash % 50 == 0:
        if count > 3:
            rem += cash + (cash * cr.AFTER_3_OPERATION_PROCENT)
            print(f'Вам начислен кешбек {cash * cr.AFTER_3_OPERATION_PROCENT} у.е.!')
        else:
            rem += cash
    else:
        top_up(rem, count)
    return rem


def take_off(rem, count):
    print('Укажите сумму для снятия кратную 50:')
    cash = input.digit_check()
    if rem >= cash + (cash * cr.TAKE_OF_PROCENT):
        if cash % 50 == 0:
            if cash * cr.TAKE_OF_PROCENT < cr.LOW_DEFAULT:
                rem -= cash + cr.LOW_DEFAULT
                print(f'Комиссия составила {cr.LOW_DEFAULT}, баланс {rem}')
            elif cash * cr.TAKE_OF_PROCENT > cr.HIGH_DEFAULT:
                rem -= cash + cr.HIGH_DEFAULT
                print(f'Комиссия составила {cr.HIGH_DEFAULT}, баланс {rem}')
            else:
                rem -= cash + (cash * cr.TAKE_OF_PROCENT)
                print(f'Комиссия составила {cash * cr.TAKE_OF_PROCENT}, баланс {rem}')
        if count > 3:
            rem += cash * cr.AFTER_3_OPERATION_PROCENT
            print(f'Вам начислен кешбек {cash * cr.AFTER_3_OPERATION_PROCENT} у.е.!')

    else:
        print('ВНИМАНИЕ! Нельзя снять сумму больше, чем остаток на счёте!')
        cr.menu(rem, count)

    return rem


def take_wealth_tax(rem):
    rem -= rem * cr.WEALTH_TAX
    print(f'Налог на богатство {rem * cr.WEALTH_TAX}, баланс {rem}')
    return rem
