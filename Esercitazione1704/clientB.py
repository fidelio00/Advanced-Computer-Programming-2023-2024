from magazzino_proxy import MagazzinoProxy
import threading, foo, socket, sys, time, random, magazzinoImpl

def runnable_func_B(host, port):
    for i in range(3):
        articoli = ("smartphone", "laptop")
        articolo = random.choice(articoli)

        print(f'[Thread B] Sto andando a prelevare un articolo di tipo {articolo} \n')
        magazzino_proxy = MagazzinoProxy(host, int(port), articolo)
        magazzino_proxy.preleva(articolo)

if __name__ == "__main__":
    try:
        host_argv = sys.argv[1]
        port_argv = int(sys.argv[2])
    except IndexError:
        print(f'Errore argomenti argv[i] \n')
        sys.exit(-1)
    
    clients_B = []

    for i in range(foo.NUM_THREADS):
        thread_client_B = threading.Thread(target=runnable_func_B, args=(host_argv, port_argv))
        thread_client_B.start()
        clients_B.append(thread_client_B)

    for i in range(foo.NUM_THREADS):
        clients_B[i].join()
    
