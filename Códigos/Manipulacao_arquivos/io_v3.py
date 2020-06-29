arquivo = open('pessoas.csv')
for dados in arquivo:  # Leitura sob demanda (streaming)
    print('Nome: {}, Idade: {}'.format(*dados.strip().split(',')))
arquivo.close()

# .strip('0') remove o elemento 0 da string
# .strip() remove os espaços em branco das laterais da str
