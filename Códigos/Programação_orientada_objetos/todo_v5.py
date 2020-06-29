from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))
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
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluido)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias.)')
        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')  # Criando um novo projeto
    casa.add('passar roupa', datetime.now() - timedelta(days=1))
    casa.add('lavar prato')
    casa.tarefas.append(TarefaRecorrente('Treino de Maconheiro',
                                         datetime.now() - timedelta(1), 7))
    casa.tarefas.append(casa.procurar('Treino de Maconheiro').concluir())
    print(casa)

    casa.procurar('lavar prato').concluir()  # Procurar tarefa, concluir tarefa
    # for tarefa in casa.tarefas: casa(projeto).tarefas(lista do projeto)
    for tarefa in casa:  # Graças ao __iter__ não preciso do .tarefas
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no Mercado')
    mercado.add('tapioca', datetime.now() + timedelta(days=3, minutes=12))
    mercado.add('amendoim')
    mercado.add('banana')
    mercado.add('bacon')
    print(mercado)

    comprar_bacon = mercado.procurar('bacon')  # Variável = tarefa bacon
    comprar_bacon.concluir()  # Concluindo a tarefa a partir da variavel
    # for tarefa in mercado.tarefas: Graças ao __iter__ não preciso do .tarefas
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
