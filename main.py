import threading
import time, random

s1 = threading._allocate_lock()
s2 = threading._allocate_lock()

def tempo(i):
   t = random.randint(1,5)
   print("Processo %i dormindo por %i" %(i, t))
   time.sleep(t)

def threading1():
   print("Processo 1 - Adquirindo semáforo S1")
   s1.acquire()
   time.sleep(1)
   print("Processo 1 - Adquirindo semáforo S2")
   s2.acquire()
   print ("Processo 1 - Seção crítica")
   tempo(1)
   print("Processo 1 - Liberando semáforos")
   s1.release()
   s2.release()
   print ("Processo 1 - seção não crítica")
   tempo(1)

def threading2():
   print ("Processo 2 - Adquirindo semáforo S2")
   s2.acquire()
   time.sleep(1)
   print ("Processo 2 - Adquirindo semáforo S1")
   s1.acquire()
   print ("Processo 2 - Seção crítica")
   tempo(2)
   print ("Processo 2 - Liberando semáforos")
   s2.release()
   s1.release()
   print ("Processo 2 - seção não crítica")
   tempo(2)

threading._start_new_thread(threading1, ())
threading._start_new_thread(threading2, ())

while 1: pass