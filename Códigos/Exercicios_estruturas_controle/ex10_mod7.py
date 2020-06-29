a = []
contador = 0

while contador < 5:
    nota = float(input('Nota do aluno: '))
    if nota in range(0, 11):
        a.append(nota)
        contador = contador + 1
        continue
    else:
        print('Valor inválido. (Sintaxe: 0 => nota =< 10)')
print(f'Média geral = {sum(a)/len(a)}')
