from concurrent import futures # Utilizzato per la gestione del pool di thread.

import grpc #La libreria gRPC per Python

# Moduli generati dal compilatore Protocol Buffers (protoc) 
# che contengono le definizioni dei messaggi e le classi di servizio.
import helloworld_pb2
import helloworld_pb2_grpc

### Crea una classe Greeter che implementa il servizio GreeterServicer
### in questo caso implementiamo il metodo SayHello

class Greeter(helloworld_pb2_grpc.GreeterServicer):
	def SayHello(self, request, context): # context è un'istanza di ServicerContext ed è standard
		print("[server] SayHello method invoked, returning response...")
		return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

### implemento il metodo serve() che sarà invocato come prima funzione dal main

def serve():
	# definisco il porto
	port = "50051"

	# mi istanzio un oggetto server da grpc
	# ALERT: i ThreadPool sono quelli del package concurrent e non multiprocess. Alcune diff in: https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	# aggiungo al server l'oggetto istanza del mio servizio Greeter
	helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

	# faccio il bind al porto impostato
	server.add_insecure_port("[::]:" + port)

	# avvio il server
	server.start()

	print("Server started, listening on " + port)

	# attendo che il server termini
	server.wait_for_termination()


if __name__ == "__main__":
	serve()
