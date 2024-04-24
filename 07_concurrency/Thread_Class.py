

#### Utilizzo class Thread

import threading

def func(id):
    print("Thread: ", id, " running\n")


if __name__ == "__main__":

    # creating thread
    t1 = threading.Thread(target=func, args=(1,))
    t2 = threading.Thread(target=func, args=(2,))
  
    # starting thread
    t1.start()
    t2.start()

    # wait until the thread finishes
    t1.join()
    t2.join()
    print("thread terminati")
    
    threads = list()
    
    for i in range(1,5):
        t = threading.Thread(target=func, args=("T"+str(i),))
        threads.append(t)
        t.start()
    
    """
        NOTA sul metodo enumerate, che ci permette di ottenere
        un oggetto enumerate che è una tupla contenente un contatore (che parte da 0 by default) 
        e i valori ottenuti iterando sopra l'oggetto target
    
        E.g.:
        seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        list(enumerate(seasons))
        [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
        list(enumerate(seasons, start=1))
        [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    """
    
    for index, t in enumerate(threads):
        print("joining thread index: ", index, "thread: ", t)

        t.join()
        

