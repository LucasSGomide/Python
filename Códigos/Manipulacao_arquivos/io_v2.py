arquivo = open('pessoas.csv')
for dados in arquivo:  # Leitura sob demanda (streaming)
    print('Nome: {} Idade: {}'.format(*dados.split(',')))
arquivo.close()
