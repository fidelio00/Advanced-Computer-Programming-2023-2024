from abc import ABC, abstractmethod

"""Questo file definisce un'interfaccia DispatcherService che viene implementata 
da altre classi per gestire l'invio e la ricezione dei comandi. 
Utilizzando l'interfaccia, possiamo garantire che qualsiasi classe 
che implementi DispatcherService abbia i metodi sendCmd e getCmd.
"""

class DispatcherService(ABC):

    @abstractmethod
    def sendCmd(self, value):
        raise NotImplementedError
        
    
    @abstractmethod
    def getCmd(self):
        raise NotImplementedError

"""
    A che serve raise NotImplementedError?
    Se una classe concreta eredita DispatcherService ma 
    non implementa sendCmd o getCmd, e viene invocato uno di questi metodi, 
    viene lanciata un'eccezione NotImplementedError. 
    Questo fornisce un feedback immediato agli sviluppatori, 
    segnalando che un metodo astratto non è stato implementato.

"""