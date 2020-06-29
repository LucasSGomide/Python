def soma_range(a, b):
    if a < b:
        lista = [num for num in range(a + 1, b)]
        return sum(lista)
    else:
        lista = [num for num in range(b + 1, a)]
        print(lista)
        return sum(lista)


print(soma_range(10, 5))
