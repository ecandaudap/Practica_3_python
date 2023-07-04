'''Función para calcular la suceción de Fibonacci'''

def fibonacci(n_digits: int):
    """La función genera una lista con los números de la serie de fibonacci.
    La función recibe la cantidad de números a generar"""

    if n_digits == 1:
        return [0]
    elif n_digits <= 0:
        return "ERROR!!! ☠☠☠"
    elif n_digits > 1:

        contador = 3

        lista_fibonacci = [0, 1]
        a_0 = 0
        a_1 = 1

        while contador <= n_digits:
            a_2 = a_0 + a_1
            a_0 = a_1
            a_1 = a_2

            lista_fibonacci.append(a_2)

            contador += 1

        return lista_fibonacci

n = int(input("Indica cuántos números de la sucesión de Fibonacci quieres ver: "))

print(fibonacci(n))
