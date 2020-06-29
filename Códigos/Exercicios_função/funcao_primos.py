def primos(a):
    primo = 0
    cont = 1
    soma = 0
    for n in range(1, a + 1):
        while cont <= a:
            soma += n
            if a % soma == 0:
                primo = primo + 1
                cont = cont + 1
            else:
                cont = cont + 1
        if primo <= 2:
            return(f'Numero {a} e primo')
        else:
            return(f'Numero {a} não e primo')


print(primos(180))
