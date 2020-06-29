with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        # 'with' Abre e já garante o fechamento do arquivo
        # 'arquivo' variável designada indiretamente
        for dados in arquivo:  # Leitura sob demanda (streaming)
            pessoa = dados.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.closed:
    print('Arquivo Fechado')

# .strip('0') remove o elemento 0 da string
# .strip() remove os espaços em branco das laterais da str
