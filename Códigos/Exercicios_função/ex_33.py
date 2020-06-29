def soma_alg(valor):
    fatorial = 1
    multiplicador = 1
    soma = 0
    for n in range(1, valor + 1):
        multiplicador *= n
    fatorial = multiplicador
    n = (str(fatorial))
    for i in range(len(n)):
        soma += int(n[i])
    return(soma)


print(soma_alg(10))
