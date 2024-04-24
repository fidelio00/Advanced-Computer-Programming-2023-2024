#### ESERCIZIO PROD_CONS con SEMAFORI con MULTITHREADING

#avere una struttura dati per la comunicazione interprocesso non è nuovo, 
#lo avete già usato in sistemi operativi quando dovevate implementare prod/cons con code di messaggo


import logging
import threading
import time
from random import randint

CONSUMER = 'Consumer'
PRODUCER = 'Producer'
N_CONSUMERS = 10
N_PRODUCERS = 10
QUEUE_SIZE = 5

# La coda la implementiamo attraverso una lista, quindi q = [], 
# perché in multithreading non c'è un concetto che astrae la coda come in multiprocess

## Logging, non è essenziale ma se lo imparate ad usare è meglio. 
logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-0s] %(message)s',)

def get_an_available_item(queue):
    return queue.pop(0)


def make_an_item_available(queue):
    item = randint(0, 100)
    queue.append(item)

    return item

# Usiamo approccio estensione classe thread
class consumerThread(threading.Thread):
    
    def __init__(self, mutex_C, empty, full, queue, name): #devo passare il mutex che uso per disciplinare i consumatori e i semafori per la cooperazione

        threading.Thread.__init__(self, name=name) #ricordate che ustilizza la lista di default
        self.mutex_C = mutex_C
        self.empty = empty
        self.full = full
        self.queue = queue

    # Ora devo sovrascrivere funzione run

    def run(self):
        logging.debug('\t\t\tStarted')

        logging.debug('\t\t\tChecking full semaphore ...')

        ####
        self.full.acquire() ### full == -1 se entra per primo il consumatore

        ### mutex.acquire()
        with self.mutex_C: ### entrerò se mutex>=0, lockare il mutex prima dell'acquire di empty è un errore perchè non consentiamo consumazioni di elementi consumabili
            logging.debug('\t\t\tAcquired mutex')
        
            time.sleep(1.0)
            item = get_an_available_item(self.queue) #sarà un metodo che possiamo implementare direttamente anche fuori (si trova all'inizio del codice)
            logging.debug('\t\t\tItem: %r', item)

            logging.debug('\t\t\tRelease mutex')
            
        ## mutex.release()
            
        self.empty.release() ### andrò a risvegliare i prod. che sono in attesa
        
        logging.debug('\t\t\tReleased empty semaphore')

        ## CONSUMER CON VAR. COND e monitor signale and continue
        """
        with self.consumer_cv:
            logging.debug('\t\t\tObtained lock')
        
            while not an_item_is_available(self.queue):
                logging.debug('\t\t\tWaiting')
                self.consumer_cv.wait() ## non posso consumare perchè non c'è spazio disp.
        
            time.sleep(1.0)
            item = get_an_available_item(self.queue)
            logging.debug('\t\t\tItem: %r', item)

            logging.debug('\t\t\tNotify')
            self.producer_cv.notify() ### notifico i produttori che sono sospesi
        """


def produce_one_item(mutex_P, empty, full, queue):
    logging.debug('Started')

    logging.debug('Checking empty semaphore...')

    empty.acquire() ### empty = 4 se sono il primo prod ad entrare

    with mutex_P: # lockare il mutex prima dell'acquire di empty è un errore perchè non consentiamo produzione di elementi producibili
        logging.debug('Acquired mutex')

        time.sleep(1.0)
        item = make_an_item_available(queue)
        logging.debug('Item: %r', item)


        logging.debug('Release mutex')
        
    full.release() ## avviserò i consumatori che sono in attesa, che possono consumare

    logging.debug('Released full semaphore')

    ## PRODUCER CON VAR. COND e monitor signal and continue
    """
    with producer_cv:
        logging.debug('Obtained lock')

        while not a_space_is_available(queue):
            logging.debug('Waiting')
            producer_cv.wait()

        time.sleep(1.0)
        item = make_an_item_available(queue)
        logging.debug('Item: %r', item)


        logging.debug('Notify')
        consumer_cv.notify()
    """


def main():
    ##Questo main sarà una funzione che non e' veramente il main, ma utilizzeremo la tecnica del name per eseguire questa funzione
    
    # generating the queue, coda fatta con una list
    queue = [] ##viene definita nello scope globale. e' un oggetto condiviso tra i thread, multiprocess non si fa più, quando creeremo process, ci sarà una copia (una fork) dal processo padre ai processi figli, quindi questo oggetto sarà copiato e poi sarà indipendente

    # Se volessi usare le var cond
    """
    cv_lock = threading.Lock()
    producer_cv = threading.Condition(lock=cv_lock) # uso un Lock per la procuder_cv, non posso usare un RLock
    consumer_cv = threading.Condition(lock=cv_lock) # uso un Lock per la consumer_cv, non posso usare un RLock
    """

    # Creiamo i semafori per gestire il problem prod/cons multipli
    #NOTA: usiamo i semafori, me ne servono 4, 2 per disciplinare la competizione tra produttori e consumatori (che sono in realtà dei mutex), 2 che devono gestire la cooperazione (uno settato alla dim, e uno a 0)
    #devo prima produrre e poi faccio il lock, perché potete produrre in maniera concorrente. Questa cosa viene risolta introducendo il buffer di stato
    
    mutex_P = threading.Semaphore() ### = 1 mutua esclusione tra i diversi prod durante la produzione
    mutex_C = threading.Semaphore() ### = 1 mutua esclusione tra i diversi cons durante la consumazione
    
    empty = threading.Semaphore(QUEUE_SIZE) ### semaforo per la produzione, inizializzato a QUEUE_SIZE (N produttori possono produrre)
    full = threading.Semaphore(0) ### semaforo per la consumazione, inizializzato a 0 (NON POSSO CONSUMARE ALL'inizio)

    consumers = []
    producers = []

    # generating the consumers
    for i in range (N_CONSUMERS):
        
        name=CONSUMER+str(i)

        # creazione del thread con estensione della classe Thread
        ct = consumerThread(mutex_C, empty, full, queue, name)
        ct.start()

        consumers.append(ct)


    # generating the producers
    for i in range (N_PRODUCERS):

        # creazione del thread con callable object (func)
        pt = threading.Thread(target=produce_one_item, name=PRODUCER+str(i),
                                args=(mutex_P, empty, full, queue),)

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
