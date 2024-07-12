
import socket, sys

def client(PORT):
 
	IP = 'localhost' #Oppure '0.0.0.0'
	BUFFER_SIZE = 1024
	MESSAGE = "Hello, World!\n"

	# La socket creata utilizza la stessa famiglia di indirizzi e lo stesso protocollo di trasporto 
 	# del server con cui si prevede di comunicare.
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
  	# Mi connetto
	s.connect((IP, PORT))

	# Codifico il codice
	s.send(MESSAGE.encode("utf-8"))

	data = s.recv(BUFFER_SIZE)

	# Stampo i dati ricevuti
	print ("received data: " + data.decode("utf-8"))


	# Chiudo la socket
	s.close()

"""
NOTA: Se mi fermassi qui, il codice funzionerebbe solo se il numero di porta (PORT) specificato nella chiamata s.connect((IP, PORT)) 
corrispondesse al numero di porta su cui il server è in ascolto. 
Tuttavia, se non si conosce il numero di porta del server, non è possibile stabilire una connessione.
Come risolviamo questo problema? Con il package sys 

"""	

if __name__ == "__main__":
	try:
		PORT = sys.argv[1]
	except IndexError:
		print("Please, specify PORT arg...")

	assert PORT != "", 'specify port'
	client(int(PORT)) #se scrivete client(PORT) avrete errore perché si aspetta un int
    

"""
Un altro modo sarebbe:

if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print("Please, specify port number...")
        sys.exit(-1) #terminate con -1 quel processo
	
	client(int(PORT))

"""
