''' Função elaborada para adicionar os numeros primos
em uma lista e depois fazer a contagem para ver quantos
numeros primos existem abaixo do valor inserido X '''


def primo_in_range(a):  # Nome da função (a <- Valor que recebe)
    lista = []  # Cria uma lista
    primo = 0  # Conta multiplos
    numero = 1  # Numero para testar se é primo
    divisor = 1  # Divisor para testar se é primo
    for n in range(1, a):  # N vai de 1 a 29
        while numero < a:  # Enquanto Numero for menor que valor recebido
            numero += n  # Adicionar numero 1 + 1
            while numero >= divisor:  # Enquanto numero for >= ao divisor
                if numero % divisor == 0:  # Se Numero/Divisor der resto 0:
                    primo += 1  # Adiciona a contagem de primos
                    divisor += 1  # Vai para o próximo divisor
                else:  # Caso não dê resto 0 a divisão:
                    divisor += 1  # Vai para o próximo divisor
            if primo <= 2:  # Se a contagem de primos for menor que 2
                lista.append(numero)  # Numero primo, adiciona na lista
                primo = 0  # Zera o contador
                divisor = 1  # Volta o divisor pra 1
            else:  # Caso não seja primo:
                primo = 0  # Zera contador
                divisor = 1  # Volta o divisor pra 1
        print(lista)  # Manda imprimir a lista
        return(f'Abaixo de {a} existem {len(lista)} numeros primos')


print(primo_in_range(30))
