def maior_fator_primo(n):
    i = 2
    lista = []
    while i * i <= n:
        print(i)
        if n % i == 0:
            lista.append(i)
            n = n / i
        else:
            i = i + 1
    print(lista)
    return(max(lista))


n = 60
print(maior_fator_primo(n))