def soma_2(a, b):
    return a + b


print(soma_2(4, 8))


def soma_3(a, b, c):
    return a + b + c


print(soma_3(10, 3, -5))


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


print(f'Soma n = {soma_n(5, 10, 65, -36, 8, 9, -25, 4)}')  # Packing
print(f'Soma n = {soma_n(5, 10, 65)}')  # Packing

tupla = (1, 3, 6, 9, 10, -7, 21, 11)
print(soma_n(*tupla))  # Unpacking
