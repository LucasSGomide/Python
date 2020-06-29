def superfatorial(valor):
    fatorial = 2
    total = 1
    while fatorial <= valor:
        a = [i for i in range(1, fatorial + 1)]
        for i in a:
            total *= i
        total = total
        fatorial += 1
    return(f'Total= {total}')
    

print(superfatorial(5))
