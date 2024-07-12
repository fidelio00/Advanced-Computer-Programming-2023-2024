from abc import ABC, abstractmethod

class IService(ABC):

    @abstractmethod
    def deposita(self, articolo, id):
        pass

    @abstractmethod
    def preleva(self, articolo):
        pass