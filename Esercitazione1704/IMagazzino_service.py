from abc import abstractmethod, ABC

class IMagazzino(ABC):
    """
    IMagazzino fornisce l'interfaccia di contratto tra client e server: fornisce due metodi che a seconda 
    che sia un Proxy o uno Skeleton vanno interpretati diversamente
    """
    @abstractmethod
    def deposita(self, articolo, id):
        raise NotImplementedError

    @abstractmethod
    def preleva(self, articolo):
        raise NotImplementedError