from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))
        # Adiciona uma nova Tarefa na lista vazia de tarefas

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError caso descricao não exista
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]
        # [0] retorna a 1ª tarefa encontrada com essa descricao
        # Se não encontrarar a tarefa retornará erro de Índice

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes)'


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
    casa = Projeto('Tarefas de Casa')  # Criando um novo projeto
    casa.add('passar roupa')  # Adicionando tarefas ao projeto
    casa.add('lavar prato')  # Adicionando tarefas ao projeto
    print(casa)

    casa.procurar('lavar prato').concluir()  # Procurar tarefa, concluir tarefa
    for tarefa in casa.tarefas:  # casa(projeto).tarefas(lista do projeto)
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no Mercado')
    mercado.add('tapioca')
    mercado.add('amendoim')
    mercado.add('banana')
    mercado.add('bacon')
    print(mercado)

    comprar_bacon = mercado.procurar('bacon')  # Variável = tarefa bacon
    comprar_bacon.concluir()  # Concluindo a tarefa a partir da variavel
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
