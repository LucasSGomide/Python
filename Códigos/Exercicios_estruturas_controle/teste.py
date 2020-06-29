def soma_lista(lista):
    return sum(lista)


lista = [1, 2, 5, 7, 8]

print(soma_lista(lista))


def inverter(parm):
    if len(parm) in range(2, 101):
        return parm[-1], parm[-2]
    else:
        return('erro')


print(inverter('aababasmstamsajhifodhfodsdsssdçlfksdpçfmsd'))
