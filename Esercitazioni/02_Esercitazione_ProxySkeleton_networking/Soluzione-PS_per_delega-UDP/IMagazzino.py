from abc import ABC, abstractmethod

# Questo file contiene l'interfaccia IMagazzino, definendo 
# i metodi astratti deposita e preleva che devono essere implementati 
# da qualsiasi classe concreta che voglia rappresentare un magazzino.

class IMagazzino(ABC):

    @abstractmethod
    def deposita(self, articolo, id_item):
        pass

    @abstractmethod
    def preleva(self, articolo):
        pass