# while True:
#     print('Vai demorar muito') - Loop eterno

# (Entre um range de números seleciona um aleatório)
from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe um Número:'))

print(f'Numero Secreto: {numero_secreto} foi encontrado ')
