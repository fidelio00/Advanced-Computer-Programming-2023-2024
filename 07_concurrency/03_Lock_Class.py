# utilizzo classe Lock

"""
Il codice utilizza la classe Lock dal modulo threading di Python per 
sincronizzare l'accesso a una risorsa condivisa, 
in questo caso la variabile x e gli attributi a e b dell'istanza della classe X.

"""

import threading
from threading import Lock
import time
 
x = 10
 
def increment(increment_by,lock):
    """
        global in Python permette di modificare la variabile al di fuori
        dello scope corrente. E' utilizzato per le variabili globali.
        Di default x senza global è locale alla funzione.
        Una var. definita al di fuori di una funzione è automaticamente global.
        global serve solo all'interno delle funzioni per variabili definite
        all'esterno di esse.
    """
    global x
 
    """
        provare a rimuovere l'acquire e il release...far vedere che se togliessi
        time.sleep alla fine funzionerebbe lo stesso anche senza proteggere
        la sez. critica...questo perchè c'è il Global Interpreter Lock che viene
        rilasciato solo per thread I/O bound (e.g., sleep)
    """

    lock.acquire()
 
    local_counter = x
    local_counter += increment_by
 
    time.sleep(1)
 
    x = local_counter
    print(f'{threading.current_thread().name} increments x by {increment_by}, x: {x}')
 
    lock.release()
 
lock = Lock()
 
# creating threads
t1 = threading.Thread(target=increment, args=(5,lock))
t2 = threading.Thread(target=increment, args=(10,lock))
 
# starting the threads
t1.start()
t2.start()
 
# waiting for the threads to complete
t1.join()
t2.join()
 
print(f'The final value of x is {x}')
