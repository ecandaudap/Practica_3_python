def select_bigger(*args) -> float:
    '''Función qué recibe varios números y 
    devuelve el mayor de ellos'''
    num = 0
    for argument in args:
        if num < argument:
            num = argument
        else:
            continue
    print(num)


select_bigger(23.7, 56.0, 17, 57, 85, 91.8, 2, 91.9, 3, 27, 66 )
