from interface import Subject
import socket, sys
import threading

# thread function
def thd_fun(c, self):

    # data received from client
    data = c.recv(1024)

    result = self.request(data) # Chiama il metodo 'request' dello Skeleton per elaborare i dati

    # send back reversed string to client
    c.send(result)

    # connection closed
    c.close()

class Skeleton(Subject):
    """
    """
    # Costruttore
    def __init__(self, port, subject):
        self.port = port # Inizializza la porta
        self.subject = subject # Inizializza il soggetto reale (istanza di RealSubject)

    def request(self, data):
        return self.subject.request(data) # Inoltra la richiesta al metodo request del soggetto reale

    def run_skeleton(self):
        
        host = 'localhost'

        # create and bind a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, self.port))
        self.port = s.getsockname()[1] # get used port

        print("Socket binded to port", self.port)

        s.listen(5)
        print("Socket is listening")

        while True:

            # establish a connection with client
            c, addr = s.accept()
            print('Connected to:', addr[0], ':', addr[1])

            # start a new thread
            t = threading.Thread(target=thd_fun, args=(c, self))
            t.start()

        s.close()

class RealSubject(Subject): # Implementa l'interfaccia Subject
    
    def request(self, data):
        # reverse the given string from client
        data = data[::-1]

        return data

if __name__ == "__main__":

    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg")
    
    print("Server running")
    realSubject = RealSubject()
    skeleton = Skeleton(int(PORT), realSubject)
    skeleton.run_skeleton()
