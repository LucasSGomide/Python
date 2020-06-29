arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close

for dados in dados.splitlines():
    #  print(dados.split(',')) -> ',' espaçamento entre a virgula e o valor
    print("Nome {} Idade {}".format(*dados.split(',')))
