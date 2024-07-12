import socket, sys, stomp, time
import multiprocess as mp
from interface import Service

# Estende mp.Process per gestire l'esecuzione di un processo separato.
# Riceve una connessione conn, un proxy proxy e un messaggio mess.
# Nel metodo run(), interpreta il messaggio per determinare se 
# è una richiesta di deposito o prelievo. 
# Utilizza il proxy per invocare il metodo appropriato (deposita o preleva) 
# e ottenere il risultato. Invia il risultato al client tramite la connessione conn.
"""
class SkeletonProcess(mp.Process):

    
    Provare ad implementare SkeletonProcess come SkeletonThread ed analizzare eventuali
    problematiche! (Suggerimento: per un numero piccolo di richiesta da parte del client
    potrebbe sembrare tutto ok...spiegare che problematica ci sarebbe.)
    
    
    def __init__(self, conn, proxy, mess):
        mp.Process.__init__(self) ### ATTENZIONE: questo è necessario!!!
        self.conn = conn
        self.proxy = proxy
        self.mess = mess


    def run(self):
        
        print(f'connection STOMP ref: {self.conn}')

        request = self.mess.split('-')[0]
        
        if request == "deposita" :
            id = self.mess.split('-')[1]
            result = self.proxy.deposita(id)
        else:
            result = self.proxy.preleva()
    
        self.conn.send('/queue/response', result)

"""
# process function

def proc_fun(conn, proxy, mess):
    
    request = mess.split('-')[0]
    
    if request == "deposita" :
        id = mess.split('-')[1]
        result = proxy.deposita(id)
    else:
        result = proxy.preleva()
    
    conn.send('/queue/response', result)


# Proxy
# Implementa l'interfaccia Service, fungendo da proxy per il server.
# Ha un costruttore che inizializza l'IP e la porta del server 
# al quale si connetterà e la dimensione del buffer per la ricezione dei dati.
class ServiceProxy(Service):
    
    def __init__(self, port):
        self.port = port
        self.ip = 'localhost'
        self.buffer_size = 1024

    def preleva(self):

        # Create the socket and connect
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        # Generate and send the request
        message = "preleva"
        s.send(message.encode("utf-8"))

        # Get the response
        data = s.recv(self.buffer_size)

        s.close()

        return data
    
    def deposita(self, id):

        # Create the socket and connect
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        # Generate and send the request
        message = "deposita-" + str(id)
        s.send(message.encode("utf-8"))

        # Get the response
        data = s.recv(self.buffer_size)

        
        s.close()

        return data


# Listener
# Implementa stomp.ConnectionListener per gestire 
# le chiamate in arrivo dal broker STOMP.
# Ha un costruttore che riceve la connessione conn e la porta port.
# Nel metodo on_message(), gestisce i messaggi in arrivo dal broker STOMP.
# Crea un'istanza di ServiceProxy per ogni messaggio in 
# arrivo e avvia un processo proc_fun per gestire la richiesta.
class MyListener(stomp.ConnectionListener):
    
    def __init__(self, conn, port):
        self.port = port
        self.conn = conn

    def on_message(self, frame):
        
        print(hex(id(frame)))
        print('[DISPATCHER] Request received: "%s"' % frame.body)

        # Generate the Proxy
        proxy = ServiceProxy(int(self.port))
        
        # Start a process to serve the request
        p = mp.Process(target=proc_fun, args=(conn, proxy, frame.body)) # callable object proc_fun
        #p = SkeletonProcess(self.conn, proxy, frame.body) # callable object proc_fun
        p.start()

# Avvio del Dispatcher:
# Legge la porta del server dalla linea di comando.
# Crea una connessione STOMP al broker locale (127.0.0.1 sulla porta 61613).
# Imposta MyListener come listener per gestire i messaggi in arrivo.
# Si connette al broker STOMP e si abbona alla coda /queue/request.
# Rimane in attesa di nuove richieste, gestite dal listener.

if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT of the server waiting of dispatcher requests")

    # Create connection
    conn = stomp.Connection([('127.0.0.1', 61613)])

    # Set the listener
    conn.set_listener('', MyListener(conn, PORT))

    # Connect and subscribe to the queue 'request'
    conn.connect(wait=True)
    conn.subscribe(destination='/queue/request', id=1, ack='auto')
    
    print("[DISPATCHER] Waiting for request ... ")

    # Keep the listener active
    while True:
        time.sleep(60)
   
