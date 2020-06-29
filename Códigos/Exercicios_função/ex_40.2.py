def pares(*args):
    a = list(args)
    impares = [impar for impar in a if impar % 2 != 0]
    print(impares)
    return(len(impares))


print(pares(3, 7, 5, 8, 6, 9, 10))
