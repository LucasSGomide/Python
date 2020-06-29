def ex_12(a):
    if a > 0:
        soma = 0
        b = str(a)
        for i in range(len(b)):
            soma += int(b[i])
        return(soma)
    else:
        return(f'Erro no Valor')


print(ex_12(1523))
