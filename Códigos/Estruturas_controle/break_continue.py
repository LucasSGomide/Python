#! python

for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

"""
O continue funciona da senguinte forma:
se o X dividido por 2 der modulo/resto = 0
o algoritimo interrompe a iteração e continua
para a próxima linha no caso imprimir o número 1.
Ex: o número 1/2 dá 0.5, gera um float, desta
forma ele irá imprimir, o 2/2 dá um int, sendo
assim, ele ira pular para a próxima iteração
no caso 'print(x)'
"""

for y in range(1, 11):
    if y == 6:
        break
    print(y)

print('fim')

"""
No caso do break ele irá interromper a iteração
quando Y == 6 , ou seja, a vaiável y será impressa
print(y) até o valor 5, chegando no 6 o 'break'
interrompe antes da iteração print(y)
"""
