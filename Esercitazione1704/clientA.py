"""
    Il client A ha lo scopo di generare 5 thread ognuno dei quali dopo t s (t scelto a caso tra 2 e 4) inoltra una una deposita
    con articolo e id scelto a caso
"""
from magazzino_proxy import MagazzinoProxy
import threading, foo, socket, sys, time, random, magazzinoImpl

def runnable_func_A(host, port):
    for i in range(3):

        articoli = ("smartphone", "laptop")
        id_a = random.randint(0,100)
        articolo = random.choice(articoli)

        print(f'[Client] Sto invocando la funzione deposita con input: \t {articolo}-{id_a}')
        magazzino_proxy = MagazzinoProxy(host, int(port), articolo, id_a)
        magazzino_proxy.deposita(articolo, id_a)



if __name__ == "__main__":
    try:
        host_argv = sys.argv[1]
        port_argv = int(sys.argv[2])
    except IndexError:
        print(f'Errore argomenti argv[i] \n')
        sys.exit(-1)
    
    clients_A = []

    for i in range(foo.NUM_THREADS):
        thread_client_A = threading.Thread(target=runnable_func_A, args=(host_argv, port_argv))
        thread_client_A.start()
        clients_A.append(thread_client_A)

    for i in range(foo.NUM_THREADS):
        clients_A[i].join()
    
