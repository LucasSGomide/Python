a = {}
contador = 0

while contador < 2:
    nome = (input('Nome do aluno: '))
    nota = (input('Nota do aluno: '))
    a.update({'Nome': nome, 'Nota': nota})
    contador = contador + 1
    continue
print(a)
print(a.get('Nota'))
