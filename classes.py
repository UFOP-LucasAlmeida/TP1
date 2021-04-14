import time, random
import threading

class FilaTarefas:
    tamanhoFila = 5
    fila = list()
    
    def __init__(self, size):
        self.tamanhoFila = size

    def inserir(self,tarefa):
        if len(self.fila) < self.tamanhoFila:
            self.fila.append(tarefa)
    
    def remover(self):
        self.fila.pop(0)

filaTarefas = FilaTarefas(5)

class Funcionario:
    id = 0
    tarefas = list()

    def __init__(self, id):
        self.id = id
        f= open("func%i.txt" %(id),"r+")
        lista = str.split(f.read()," ")
        for tarefa in lista:
            self.tarefas.append([id,tarefa])

class Maquina:
    id = 0
    idFuncionario = 0
    idTarefa = 0
    tempoTarefa = 0
    global filaTarefas

    def __init__(self,idM):
        self.id = idM

    def executarThread(self):
        t = threading.Thread(target = self.executarProximaTarefa)
        t.start()

    def executarProximaTarefa(self):
        tarefa = self.filaTarefas.fila[0]
        time.sleep(tarefa[2])
        print("Exec", self.id, tarefa[0])
