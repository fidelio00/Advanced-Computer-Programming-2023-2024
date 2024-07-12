import socket
import threading

# thread function -> Definisce una funzione che verrà eseguita in un thread separato. 
# c rappresenta la socket del client.
def thd_fun(c):


    # data received from client
    data = c.recv(1024)

    # reverse the given string from client
    data = data[::-1]

    # send back reversed string to client
    c.send(data)

    # connection closed
    c.close()


if __name__ == '__main__':

    host = "" #Specifica che il server ascolterà su tutte le interfacce di rete disponibili.
    cur_port = 0 #Utilizza una porta qualsiasi disponibile.

    # create and bind a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, cur_port))
    cur_port = s.getsockname()[1] # get used port

    print("Socket binded to port", cur_port)

    s.listen(5) #Permette fino a 5 connessioni pendenti
    print("Socket is listening")

    while True:

        # establish a connection with client
        c, addr = s.accept()
        print('Connected to :', addr[0], ':', addr[1])

        # start a new thread
        t = threading.Thread(target=thd_fun, args=(c,))
        t.start()

    s.close()


