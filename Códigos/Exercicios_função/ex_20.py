def fatorial(a):
    fatorial = 1
    for n in range(1, a + 1):
        fatorial *= n
    fatorial = fatorial
    return(fatorial)


print(fatorial(5))
