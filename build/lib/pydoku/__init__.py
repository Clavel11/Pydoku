def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y


def suma_alternada(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            #impares
            suma = suma + i**2
        else:
            #pares
            suma = suma - i**2
    return suma
