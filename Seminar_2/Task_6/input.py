def digit_check():
    try:
        number = int(input('\n'))
        return number
    except ValueError:
        print('Это должно быть число\n')
        return digit_check()