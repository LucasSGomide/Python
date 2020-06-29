a = []
contador = 0

while contador < 5:
    a.append(int(input('Digite um número: ')))
    contador = contador + 1
    continue
print('Lista = ', a)

print(f'Maior número = {max(a, key=int)}')
print(f'Index do número = {a.index(max(a, key=int))}')
print(f'Menor número = {min(a, key=int)}')
