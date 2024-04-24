## Esempio di uso del RLock, ovvero metodo di una classe che usa un lock su cui c'è un lock di un'altro
## metodo che viene invocato

import threading

"""
Viene definita una classe X che contiene due attributi, a e b, e un oggetto Lock
"""

class X:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.RLock() # provare a cambiare RLock in Lock e vedere cosa accade...

    """ 
    I metodi changeA e changeB modificano rispettivamente gli attributi a e b 
    dell'istanza di X, utilizzando il blocco with self.lock 
    per sincronizzare l'accesso ai dati condivisi
    """
    def changeA(self):
        with self.lock:
            self.a = self.a + 1

    def changeB(self):
        with self.lock:
            self.b = self.b + self.a

    """ 
    il metodo changeAandB chiama i metodi changeA e changeB 
    all'interno di un unico blocco with self.lock, garantendo che 
    entrambi i cambiamenti avvengano in modo atomico e sincronizzato.
    """
    
    def changeAandB(self):
        # you can use chanceA and changeB thread-safe!
        with self.lock:
            self.changeA() # a usual lock would block at here
            self.changeB()


x = X()
print('a:', x.a)
x.changeA()

print('a dopo changeA: ', x.a)
print('b:', x.b)
x.changeB()

print('b dopo changeB: ', x.b)
x.changeAandB()

print('a dopo changeAandB: ', x.a, 'b dopo changeAandB: ', x.b)

