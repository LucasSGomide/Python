def fatorial_exp(valor):
    pot = valor - 1
    pot = pot
    while pot >= 1:
        valor **= pot
        total = valor
        pot -= 1
    return(total)


print(fatorial_exp(5))
