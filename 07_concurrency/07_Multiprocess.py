### Uso di multiprocessing/multiprocess callable object
### NOTA: in jupiter notebook multiprocessing non funziona
### installare multiprocess che è la stessa cosa (pip install multiprocess)

import multiprocess as mp

def func():
   print ('Process running')
   return


if __name__ == '__main__':

    # creating process
    p = mp.Process(target = func)

    # starting process
    p.start()

    # wait until the process finishes
    p.join()

    print("all joined")

"""
NOTA: Il motivo per cui non vedi "Process running" stampato potrebbe essere dovuto a un problema di sincronizzazione delle stampe tra processi. 
In Python, quando si utilizzano processi multipli con il modulo multiprocessing, ogni processo ha il proprio spazio di stampa separato. 
Pertanto, le stampe effettuate all'interno del processo figlio non saranno visibili direttamente nel processo genitore, 
a meno che non si utilizzino metodi specifici per comunicare tra i processi.
"""

---------------------------------------------------------------------------------------------------------------

### Uso di multiprocessing/multiprocess con class

import multiprocess as mp

class MyProcess(mp.Process):

    def run(self):
       print ('Process running')
       return

if __name__ == '__main__':

    # creating process
    p = MyProcess()

    # starting process
    p.start()

    # wait until the process finishes
    p.join()

--------------------------------------------------------------------------------------------------------------------

from multiprocess import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()

---------------------------------------------------------------------------------------------------------------------

### uso di multiprocess Pipe

"""
Una Pipe in Python è un meccanismo di comunicazione bidirezionale che permette lo scambio di dati tra processi. 
È costituita da due endpoint, uno per il processo genitore e uno per il processo figlio. 
I processi possono scrivere dati in un endpoint e leggerli dall'altro. 
La classe Pipe del modulo multiprocessing crea una Pipe e restituisce due oggetti connessione che rappresentano i due endpoint.

"""

from multiprocess import Process, Pipe

def parentData(parent):
    parent.send(['Hello'])
    parent.close()
    
def childData(child):
    child.send(['Bye'])
    child.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p1 = Process(target=parentData, args=(parent_conn,))
    p1.start()
    p2 = Process(target=childData, args=(child_conn,))
    p2.start()
    print(parent_conn.recv()) #il parent riceve Bye
    print(child_conn.recv())  #il child riceve Hello 
    p1.join()
    p2.join()

-------------------------------------------------------------------------------------------------------------------------

## uso di multiprocess Queue

from multiprocess import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()

----------------------------------------------------------------------------------------------------------------------------

### uso di multiprocess shared memory

# Value viene utilizzata per creare una variabile condivisa tra i processi 
# Array viene utilizzata per creare un array condiviso tra i processi.
from multiprocess import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])


