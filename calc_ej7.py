"""Escribe un programa que emule el funcionamiento de una calculadora simple. 
Este es un posible ejemplo de la ejecución del programa en una terminal"""


def calc():
    """Programa que emula a una calculadora simple.
    Se iniciliza con un número y se debe poner la operación y el número correspondiente.
    Se finaliza con el signo =.
    Si se pone el número sin la operación, la calculadora se reinicia.
    Los resultados se van mostrando parcialmente, hasta el resultado final."""

    total = 0
    continuar = True

    while continuar:
        op_num = input("Ingresa operación/número: ")
        if op_num == "=":
            continuar = False
        else:
            if op_num.isnumeric():
                op_num = float(op_num)
                total = op_num
            elif (op_num.isnumeric() is False) & (op_num[0] in "+"):
                total += float(op_num[1:])
                print(f"Resultado parcial = {total}")
            elif (op_num.isnumeric() is False) & (op_num[0] in "-"):
                total -= float(op_num[1:])
                print(f"Resultado parcial = {total}")
            elif (op_num.isnumeric() is False) & (op_num[0] in "*"):
                total *= float(op_num[1:])
                print(f"Resultado parcial = {total}")
            elif (op_num.isnumeric() is False) & (op_num[0] in "/"):
                total /= float(op_num[1:])
                print(f"Resultado parcial = {total}")

    # print(f'TOTAL = {total}')
    return total


print(calc())
