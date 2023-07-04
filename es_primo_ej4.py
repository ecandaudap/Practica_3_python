def isprime(num: int):
    '''Función que permite identificar si un número dado es primo o no.
       Devuelve un booleano. True si es primo y False si no lo es'''

    if (num % 2 != 0) & (num % 3 != 0) & (num % 5 != 0) & (num % 7 != 0) & (num % 11 != 0) & (num % 13 != 0):
        print(True)
    else:
        print(False)

number = int(input("Ingresa un número entero del 1 al 100 para saber si es primo: "))  

isprime(number)