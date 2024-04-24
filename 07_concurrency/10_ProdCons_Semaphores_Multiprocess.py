#### ESERCIZIO PROD_CONS con SEMAFORI con MULTIPROCESS

import logging
import multiprocess
from multiprocess import Queue
import time
from random import randint

CONSUMER = 'Consumer'
PRODUCER = 'Producer'
N_CONSUMERS = 10
N_PRODUCERS = 10
QUEUE_SIZE = 1

#logging.basicConfig(level=logging.DEBUG, format='%(message)s',)

def get_an_available_item(queue):
    return queue.get()


def make_an_item_available(queue):
    item = randint(0, 100)
    queue.put(item)

    return item


class consumerProcess(multiprocess.Process):
    
    def __init__(self, queue, name):

        multiprocess.Process.__init__(self, name=name)
        self.queue = queue

    def run(self):
     
            time.sleep(1.0)
            item = get_an_available_item(self.queue)
            print(f'[PID: {multiprocess.current_process().pid}] \t\t\tConsumed Item: {item}\n')
        
            
        

def produce_one_item(queue):
    
        time.sleep(1.0)
        item = make_an_item_available(queue)
        print(f'[PID: {multiprocess.current_process().pid}] Produced Item: {item}\n')


def main():
    
    # generating the queue, coda fatta con una list
    queue = Queue(QUEUE_SIZE)

    consumers = []
    producers = []
    #multiprocess.set_start_method("spawn")
    
    # generating the consumers
    for i in range (N_CONSUMERS):
        
        name=CONSUMER+str(i)

        # creazione del process con estensione della classe Process
        ct = consumerProcess(queue, name)
        ct.start()

        consumers.append(ct)


    # generating the producers
    for i in range (N_PRODUCERS):

        # creazione del process con callable object (func)
        pt = multiprocess.Process(target=produce_one_item, name=PRODUCER+str(i),
                                args=(queue,))

        pt.start()

        producers.append(pt)    

    
    # waiting consumers termination
    for i in range (N_CONSUMERS):

        consumers[i].join()


    # waiting producers termination
    for i in range (N_PRODUCERS):

        producers[i].join()



if __name__ == '__main__':
    main()
