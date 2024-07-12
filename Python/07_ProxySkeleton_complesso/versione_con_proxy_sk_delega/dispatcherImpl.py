from dispatcher_service import DispatcherService
import multiprocess as mq

"""
Questo file contiene l'implementazione concreta della classe che gestisce 
l'invio e la ricezione dei comandi, utilizzando una coda condivisa. 
La classe dispatcherImpl implementa l'interfaccia DispatcherService.
"""

## implementazione di Subject
class dispatcherImpl(DispatcherService): # RealSubject estende Skeleton che implementa Subject (il mio servizio)

    def __init__(self, queue=mq.Queue(5)): #istanza di multiprocessing.Queue che serve da coda per memorizzare i comandi.
        self.queue = queue

    def sendCmd(self, value): # Aggiunge un comando alla coda
        #print(f'[dispatcherImpl sendCmd] ref to queue: {self.queue}')
        self.queue.put(value)
    
    def getCmd(self): #estrae un comando dalla coda
        value_to_get = self.queue.get()
        #print(f'[dispatcherImpl getCmd] ref to queue: {self.queue} value get: {value_to_get}')
        return value_to_get
