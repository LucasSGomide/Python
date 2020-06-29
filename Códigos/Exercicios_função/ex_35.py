def fatorial_quadruplo(valor):
    mult = 1
    mult_2 = 1
    quadruplo = valor * 2
    a = [n for n in range(1, quadruplo + 1)]
    b = [i for i in range(1, valor + 1)]
    for n in a:
        mult *= n
    total = mult
    for i in b:
        mult_2 *= i
    total_2 = mult_2
    return(total/total_2)


print(fatorial_quadruplo(5))
