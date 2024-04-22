from IMagazzino_service import IMagazzino
from abc import ABC, abstractmethod
import threading, foo, socket, sys, time

def run_function(conn, skeleton):
    print(f'[Thread Server] Creato correttamente... \n')
    data_received = (conn.recv(foo.BUFFER_SIZE)).decode("utf-8")

    print(f'[Thread Server] Dati ricevuti: \t {data_received}')

    result = "Errore"

    ###devo identificare ora il tipo di comando che mi è stato inviato per invocare il giusto metodo
    articolo_to_deposit = (data_received).split("-")[1] ##assumo che il formato sia: type_request-articolo-id(opzionale)
    if "deposita" in data_received:
        ##print(f'[Skeleton Server] Il client ha chiesto di deposita larticolo {articolo_to_deposit} con id {(data_received).split("-")[2]}')
        skeleton.deposita(articolo_to_deposit, (data_received).split("-")[2])
        result = "OK"

    else:
        articolo_da_prelevare = data_received.split("-")[1]
        print(f'[Skeleton Server] arrivata una richiesta di prelievo di {articolo_da_prelevare}... \n')
        result = skeleton.preleva(articolo_da_prelevare)


    print(f'[Server] Invio resoconto operazione al client... \n')
    conn.send(result.encode("utf-8"))
    conn.close()
    



class MagazzinoSkeleton(IMagazzino):
    """
    MagazzinoSkeleton(IMagazzino) rappresenta lo Skeleton del Server magazzino, avrà il compito di mettersi in ascolto
    di richieste da parte dei clients e per ognuna di essa creare un Thread (nella funzione run_skeleton())
    che smisterà correttamente la richiesta richiamando il giusto metodo, che verrà definito poi in
    MagazzinoImpl.py
    """
    def __init__(self, host, port):
        ##host e port sono necessari: devo creare correttamente la socket Main Server
        self.host = host
        self.port = port

    @abstractmethod
    def deposita(self, articolo, id):
        pass
    @abstractmethod
    def preleva(self, articolo):
        pass

    def run_skeleton(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))

        print(f'[Server] Socket binded to {s.getsockname()[0]}  {s.getsockname()[1]}')
        s.listen(30)

        while True:
            conn, addr = s.accept()
            print(f'[Server] Accettata la richiesta da parte del client {addr}')

            ##creo un thread che si occupi della parte di gestione business logic
            my_thread = threading.Thread(target = run_function, args = (conn, self))
            my_thread.start()

        s.close()