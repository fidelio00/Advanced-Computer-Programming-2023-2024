"""
    Devo implementare la parte applicativa del magazzino. Nel pattern proxy/Skeleton con ereditarietà:
"""
import socket, sys, time, threading
from abc import ABC, abstractmethod
from magazzinoSkeleton import MagazzinoSkeleton
import multiprocess as mp

class MagazzinoImpl(MagazzinoSkeleton):
    def __init__(self, host, port, queue_laptop = mp.Queue(5), queue_smartphone = mp.Queue(5)):
        super().__init__(host, port)
        self.queue_laptop = queue_laptop
        self.queue_smartphone = queue_smartphone
    
    def deposita(self, articolo, id):
        if "smartphone" in articolo:
            self.queue_smartphone.put(id)
            print(f'[Magazzino] Articolo con id {id} depositato correttamente!')
        else:
            self.queue_laptop.put(id)

    def preleva(self, articolo):
        if  "smartphone" in articolo:
            articolo_prelevato = str(self.queue_smartphone.get())
            ##apro il file in modalità append altrimenti mi elimina tutto ciò che c'era prima
            with open("smartphone.txt", mode = "a") as smartphone_file:
                smartphone_file.write(f'{articolo_prelevato} \n')

            return articolo_prelevato
        else:
            articolo_prelevato = str(self.queue_laptop.get())
            with open("laptop.txt", mode = "a") as laptop_file:
                laptop_file.write(f'{articolo_prelevato} \n')
            return articolo_prelevato
