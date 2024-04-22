from IMagazzino_service import IMagazzino
import socket
import threading
import random, sys
from time import sleep

##devo scrivere la logica di comunicazione tra client e server qui:

class MagazzinoProxy(IMagazzino):
    """
    MagazzinoProxy implementa il contratto lato Client (ovvero il Proxy): definisce i due metodi astratti
    di IMagazzino_service. Il client creerà un oggetto di tipo MagazzinoProxy per ogni richiesta (Client multi-thread)
    """
    
    def __init__(self, ip_dest, port_dest, articolo, id = 0):
        self.ip_dest = ip_dest
        self.port_dest = port_dest
        self.articolo = articolo
        self.id = id

    def deposita(self, articolo, id):
        """
        deposita si connette col server indicato nei parametri e gli passsa una stringa
        SUPPONGO SIA UNA SOCKET TCP
        """
        BUFFER_SIZE = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip_dest, self.port_dest))
        request = str("deposita"+"-"+str(self.articolo)+"-"+str(self.id))
        sleep(random.randint(2,4))

        print(f'[Thread Client A] Sto inviando al Server {s.getsockname()[0]} \t {s.getsockname()[1]} la seguente richiesta di deposito: \t {request}')
        s.send(request.encode("utf-8"))
        print(f'Richiesta inviata... \n')

        ##mi metto in ricezione di una risposta..
        data = s.recv(BUFFER_SIZE)
        print(f'[Thread Client A] Ricevuta risposta: \t {data.decode("utf-8")}')
        s.close()

    def preleva(self, articolo):
        """
        Nel caso che un client chiami la funzione "preleva" andrà a prelevare l'elemento dalla coda
        e poi stamparlo a video.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip_dest, self.port_dest))
        request = str("preleva"+"-"+str(articolo))

        sleep(random.randint(2,4))

        print(f'[Thread Client B] Sto prelevando.... \n')
        s.send(request.encode("utf-8"))

        data = s.recv(1024)
        print(f'[Thread Client B] Ricevuta risposta dal server: \t {data.decode("utf-8")}')
        s.close()