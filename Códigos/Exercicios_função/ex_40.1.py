def pares(*args):
    a = list(args)
    print(a)
    for n in a:
        if n % 2 != 0:
            a.remove(n)
    print(a)
    return len(a)


print(pares(1, 3, 5, 81, 6, 9, 10))