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

    def __init__(self, id):
        self.id = id
        self.tarefas = []
        f= open("func%i.txt" %(id),"r+")
        lista = f.readlines()
        f.close()
        for tarefa in lista:
            tarefa = tarefa.replace('\n', '')
            self.tarefas.append([id] + tarefa.split(" "))
                    
class Maquina:
    id = 0
    idFuncionario = 0
    idTarefa = 0
    tempoTarefa = 0
    global filaTarefas

    def __init__(self,idM):
        self.id = idM

    def executarThread(self):
        t = threading.Thread(target = self.executarTarefas)
        t.start()

    def executarTarefas(self):
        while len(filaTarefas.fila) > 0:
            tarefa = filaTarefas.fila[0]
            filaTarefas.remover()
            time.sleep(tarefa[2])
            print("Exec", self.id, tarefa[0])
