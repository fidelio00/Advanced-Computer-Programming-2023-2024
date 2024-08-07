from MagazzinoImpl import MagazzinoImpl
from MagazzinoSkeleton import MagazzinoSkeleton

# Questo file avvia il server, istanzia MagazzinoImpl e 
# MagazzinoSkeleton, e avvia lo skeleton

IP = "localhost"
PORT = 0
QUEUE_SIZE = 5

# Creo una istanza del servizio reale e dello Skeleton, dato che lo Skeleton è per delega
# ed avvio lo skeleton
magazzino = MagazzinoImpl(QUEUE_SIZE)
skeleton = MagazzinoSkeleton(IP, PORT, magazzino)
skeleton.runSkeleton()

print("[MAGAZZINO SERVER] Started")