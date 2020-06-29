#! python
palavra = 'paralelepípedo'

for letra in palavra:
    print(letra, end=' ')
print('Fim')

aprovados = ['Rafaela', 'Pedro', 'Renata', 'Maria']
reprovados = ['Lucas', 'Rodrigo', 'Franciso', 'Eliezer']

for posicao, nome_aprovados in enumerate(aprovados):
    print(f'Aprovados: {posicao + 1})', nome_aprovados)

for posicao, nome_reprovados in enumerate(reprovados):
    print(f'Reprovados: {posicao + 1})', nome_reprovados)

dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta'
               'Quinta', 'Sexta', 'Sábado', 'Domingo')

for dia in dias_semana:
    print(f'Hoje é: {dia}')

for letra in set('muito legal'):
    print(letra)

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
