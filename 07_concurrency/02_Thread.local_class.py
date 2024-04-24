#### Utilizzo class Thread.local

import threading
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-0s)%(message)s',)

def show(d):
    try:
        val = d.val
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)

def f(d):
    show(d)
    d.val = random.randint(1, 100)
    show(d)

if __name__ == '__main__':
    d = threading.local()
    show(d)
    d.val = 999
    show(d)

    for i in range(2):
        t = threading.Thread(target=f, args=(d,))
        t.start()


----------------------------------------------------

#Stesso codice ma senza usare logging

import threading

def func(id):
    print("Thread: ", id, "running \n")

if __name__ == "__main__":
    
    threads = list()
    
    for i in range(1,5):
        t= threading.Thread(target=func,args=("T"+str(i),))
        threads.append(t)
        t.start()

    for index, t in enumerate(threads):
        print("joining thread index: ", index, "thread: ", t)
        t.join()
