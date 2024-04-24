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
