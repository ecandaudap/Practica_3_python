def multiply(*args) -> float:
    '''Función qué permite multiplicar varios números'''
    num = 1
    for argument in args:
        num *= argument
    print(num)


multiply(23.7, 56.8, 17, 57)