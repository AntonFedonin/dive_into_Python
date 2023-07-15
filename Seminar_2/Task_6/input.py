def digit_check():
    try:
        lenght = int(input('\n'))
        return lenght
    except ValueError:
        print('Это должно быть число\n')
        return digit_check()