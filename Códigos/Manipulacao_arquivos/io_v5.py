with open('pessoas.csv') as arquivo:
    # 'with' Abre e já garante o fechamento do arquivo
    # 'arquivo' variável designada indiretamente
    for dados in arquivo:  # Leitura sob demanda (streaming)
        print('Nome: {}, Idade: {}'.format(*dados.strip().split(',')))

if arquivo.closed:
    print('Arquivo Fechado')

# .strip('0') remove o elemento 0 da string
# .strip() remove os espaços em branco das laterais da str
