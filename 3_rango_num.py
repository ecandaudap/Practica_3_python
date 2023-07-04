def isinrange(inf: float, sup: float, num: float):
    '''Función para verificar que un número se encuentra en 
    un rango de números determinado. Devuelve un booleano. 
    True si el número está dentro el rango y 
    False si no se encuentra dentro del mismo'''

    if (num >= inf) and (num <= sup):
        print(True)
    else:
        print(False)

inferior = float(input("Ingresa el límite inferior de un rango de números: "))
superior = float(input("Ingresa el límite superior de un rango de números: "))
number = float(input("Ingresa un número para saber si está dentro del rango elegido: "))  

isinrange(inferior, superior, number)