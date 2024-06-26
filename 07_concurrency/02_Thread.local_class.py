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
import random

def show(d):
    try:
        val = d.val
    except AttributeError:
        print('No value yet')
    else:
        print('value =', val)

def f(d):
    show(d)
    d.val = random.randint(1, 100)
    show(d)

if __name__ == '__main__':
    d = threading.local() #Crea un oggetto local dalla classe threading, che fornisce uno spazio dei nomi separato per ciascun thread.
    show(d)
    d.val = 999
    show(d)

    for i in range(2):
        t = threading.Thread(target=f, args=(d,))
        t.start()
