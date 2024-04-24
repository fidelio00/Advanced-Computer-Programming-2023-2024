### Uso della classe Semaphore

from threading import *
from time import sleep
from random import random

# creating thread instance where count = 3
obj = Semaphore(3)

def display(name):

    obj.acquire()
    
    value = random()
    sleep(value)
    print(f'Thread {name} got {value}')

    obj.release()

if __name__ == '__main__':

    threads = []

    # creating and starting multiple threads
    for i in range(10):
        t = Thread(target = display , args = ('Thread-' + str(i),))
        threads.append(t)
        t.start()

    # wait for the threads to complete
    for thread in threads:
        print(thread)
        thread.join()
