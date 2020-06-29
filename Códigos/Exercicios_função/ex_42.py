def inteiros(*args):
    qntd = len(args)
    soma = sum(args)
    return(round(soma/qntd, 2))


print(inteiros(3, 7, 5, 8, 6, 9, 10))
