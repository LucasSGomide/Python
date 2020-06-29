def mdc_primo(n_recebido):
    lista = []
    n_atual = n_recebido
    divisor = 1
    while divisor <= n_recebido:
        if n_atual % divisor == 0:
            lista.append(divisor)
            n_atual = n_atual / divisor
            divisor = 2
        else:
            divisor += 1
    print(lista)
    return(max(lista))


print(mdc_primo(20))
