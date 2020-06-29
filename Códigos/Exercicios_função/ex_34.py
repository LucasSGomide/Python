def fatorial_duplo(valor):
    soma = 1
    a = [n for n in range(1, valor + 1) if n % 2 != 0]
    for n in a:
        soma *= n
    return(soma)


print(fatorial_duplo(5))