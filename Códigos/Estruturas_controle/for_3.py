#! python

produto = {'Nome:': 'Aveia', 'Preço': 4.99,
           'Nacional': True, 'Estoque:': 10}

for chave in produto.keys():
    print(chave)

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave, valor)

"""
Este ultimo print remete  a uiltima variável apresentada
ou sejam o resultado será 'Estoque: 10' pois o python
armazena as informações, isto vale para as situações
anteriores também.
"""
