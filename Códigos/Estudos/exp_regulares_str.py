import re

test = 'This is for testing regular expressions in Python.'

result = re.search('This', test)  # Método para fazer a procura

print(result.group())  # Resultado da procura (This)

result = re.match('This', test)  # Procura na 1ª palavra
print(result)

print(result.group(0))

result = re.match('regular', test)  # Não encontra -> só procura na 1ª palavra
print(result)

result = re.match('(.{20})(regular)', test)  # Add 20 espaços p/ pesquisa
print(result.group(0))  # Mostra o resultado completo
print(result.group(1))  # Mostra 'This is for testing '
print(result.group(2))  # Mostra 'regular'


teste = 'Este e para encontrarmos expressoes regulares'
print(len(teste))
resultado = re.match('(.{36})(regulares)', teste)
print(resultado.group(0))
print(resultado.group(1))
print(resultado.group(2))
