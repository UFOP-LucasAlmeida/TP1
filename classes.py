import time, random
import threading

class FilaTarefas:
    tamanhoFila = 5
    mutex  = threading.Semaphore(1)
    empty  = threading.Semaphore(tamanhoFila)
    full   = threading.Semaphore(0)
    buffer = list(range(tamanhoFila))
    cheio  = 0
    livre  = 0

    def __init__(self, size):
        self.tamanhoFila = size

    def insert(self, item):
        self.empty.acquire()
        self.mutex.acquire()
        self.buffer[self.livre] = item
        self.livre = (self.livre + 1) % self.tamanhoFila
        self.mutex.release()
        self.full.release()

    def remove(self):
        self.full.acquire()
        self.mutex.acquire()
        item = self.buffer[self.cheio]
        self.cheio = (self.cheio + 1) % self.tamanhoFila
        self.mutex.release()
        self.empty.release()
        return item

b = FilaTarefas()

def produtor():
   while True:
      time.sleep(random.randint(1, 10) / 100.0)
      item = time.ctime()
      b.insert(item)
      print("Produtor produziu:", item, b.livre, b.cheio)

def consumidor():
   while True:
      time.sleep(random.randint(1, 10) / 100.0)
      item = b.remove()
      print("Consumidor consumiu:", item, b.livre, b.cheio)

threading._start_new_thread(produtor, ())
threading._start_new_thread(consumidor, ())

while 1: pass