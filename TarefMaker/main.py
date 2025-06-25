class Tarefa:
    def __init__(self, nome, descricao, prazo):
        self.nome = nome
        self.descricao = descricao
        self.prazo = prazo
        self.status = "Não Iniciada"

    def marcar_fazendo(self):
        self.status = "Em progesso"

    def marcar_concluida(self):
        self.status = "Concluída"

    def editar(self, nome=None, descricao=None, prazo=None):
        if nome:
            self.nome = nome
        if descricao:
            self.descricao = descricao
        if prazo:
            self.prazo = prazo

class GerenciadoDeTarefa:
    def __init__ (self):
        self.lista = []

    def adicionar_tarefa(self, nome, descricao, prazo):
        tarefa = Tarefa(nome, descricao, prazo)
        self.lista.append(tarefa)

    def remover_tarefa(self, nome):
        self.lista = [t for t in self.lista if t.nome != nome]

    def listar_tarefas(self):
        for tarefa in self.lista:
            print(f'Nome: {tarefa.nome}, Status: {tarefa.status}, Prazo: {tarefa.prazo}')

    def feito(self, nome):
        for tarefa in self.lista:
            if tarefa.nome == nome:
                tarefa.marcar_concluida()

gerenciador = GerenciadoDeTarefa()
gerenciador.adicionar_tarefa('teste', 'teste de tarefa', '12/06')
gerenciador.listar_tarefas()
gerenciador.feito('teste')
gerenciador.listar_tarefas()