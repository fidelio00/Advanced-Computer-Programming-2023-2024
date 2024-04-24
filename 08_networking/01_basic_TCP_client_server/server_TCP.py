import socket

#Setto una variabile IP sul quale il server si mette in attesa di nuove connessioni
IP = '0.0.0.0' #serve per indicare 'localhost', potreste anche scrivere direttamente 'localhost' ma alcune volte non funziona
PORT = 0

# Nella ricezione, con recv(bufsize), potete mettervi in attesa bloccante di dati su una determinata dimensione massima
BUFFER_SIZE = 1024 #Quindi 1 kb

# Creo una socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET -> ipv4, socket.SOCK_STREAM -> socket di tipo TCP
# Se la creazione fallisce la creazione, s sarà impostato uguale a None
# Si scatenerebbe un'eccezione OSError perché sto invocando una systemcall


# s.bind(address) -> address è la tupla (IP, porto) 
# Si potrebbe anche prima scrivere address = (IP,PORT)
s.bind((IP, PORT))

# Usiamo la listen per abilitare il server ad accettare una nuova connessione
# Se non chiamiamo la listen prima dell'accept, fallirà di nuovo con una OSError
s.listen(1)

# getsockname -> per ricavare l'address di quella socket, dalla quale possiamo recuperare il numero id porto
print("getsockname: ", str(s.getsockname())) # Restituisce una tupla, il porto è all'elemento 1
cur_port = s.getsockname()[1] #get used port
print("server on: ", IP, "port: ", cur_port)

# Questa accept è la chiamata alla funzione che accetta una connessione
conn, addr = s.accept()


print("client addr: " + str(addr))
print  ('Connection address: {}' .format(addr))

# Ricevo i dati
data = conn.recv(BUFFER_SIZE) # Ricorda: abbiamo importato massimo 1kb in ricezione dal lato client

# Codifichiamo questi dati su un certo formato. La codifica unicode, quindi utf, è quella più comoda
# utf-8 è la codifica unicode su 8 bit
print ("received data: " + data.decode("utf-8"))

# Inviamo un messaggio
toClient= "The world never says hello back!\n"
conn.send(toClient.encode("utf-8"))
 
conn.close() # Chiudo la connessione
s.close() # Chiudo la socket
