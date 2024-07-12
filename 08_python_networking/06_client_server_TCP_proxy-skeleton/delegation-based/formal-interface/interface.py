from abc import ABC, abstractmethod
# ABC è una classe base fornita dal modulo abc che permette di definire classi astratte.
# abstractmethod è un decoratore utilizzato per dichiarare metodi 
# astratti all'interno di una classe astratta.

class Subject(ABC): 
    #Subject è una classe che eredita da ABC, il che la rende una classe astratta. 
    # Una classe astratta non può essere istanziata direttamente. 
    # Serve come base per altre classi.

    @abstractmethod #è un decoratore che rende il metodo request un metodo atratto
    def request(self, data):
        pass