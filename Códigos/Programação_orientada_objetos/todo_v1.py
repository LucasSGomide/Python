from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluiida)' if self.feito else '')
    # Método p/ STRING não precisa ser chamado executará direto caso self.feito
    # for True. Ou seja, se o concluir for executado o método __str__ será auto
    # maticamente acionado e gerará a string descricao da tarefa + status


def main():
    casa = []
    casa.append(Tarefa('Passar Roupa'))  # Adicionando OBJETOS criados com
    casa.append(Tarefa('Lavar Prato'))  # a classe tarefa

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar Prato']
    # List comprehension - sem criar variável e executando o método concluir()

    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
