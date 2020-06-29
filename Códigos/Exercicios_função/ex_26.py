'''Funções para somar todos os algarismos anteriores
ao numero fornecido pelo usuário.
Obs: implantar INPUT. '''


def soma(n):
    soma = 0
    for numeros in range(1, n + 1):
        soma += numeros
    return(soma)


print(soma(50))


def soma_2(n):
    lista = list(range(1, n + 1))
    lista = sum(lista)
    total = str(lista)
    return(total)


print(soma_2(50))
