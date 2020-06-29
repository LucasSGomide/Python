# Variáveis

a = {}
limite = 0

# Preenchendo o dicionário:
while limite < 5:
    a[str(input('Matrícula: '))] = float(input('Altura em M: '))
    limite = limite + 1

# Variáveis 2

maior = list(a.values())
maior = float(max(maior, key=float))

menor = list(a.values())
menor = float(min(menor, key=float))

# Filtrar as informações

for chave, valor in a.items():
    for itens in chave:
        if valor == maior:
            print(f'Mais alto = Matricula: {itens} altura {maior}')

for chave_2, valor_2 in a.items():
    for itens_2 in chave_2:
        if valor_2 == menor:
            print(f'Mais baixo = Matricula: {itens_2} altura {menor}')
