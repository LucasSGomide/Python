def pares(*args):
    a = list(args)
    pares = [par for par in a if par % 2 == 0]
    print(pares)
    return(len(pares))


print(pares(3, 7, 5, 8, 6, 9, 10))
