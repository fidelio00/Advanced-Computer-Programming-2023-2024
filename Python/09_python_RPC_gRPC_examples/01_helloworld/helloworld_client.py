# Questa direttiva garantisce che la funzione print sia 
# compatibile con Python 3 anche se eseguita in Python 2
from __future__ import print_function

import logging # gestisce messaggi di log

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def run():
	# NOTE(gRPC Python Team): .close() is possible on a channel and should be
	# used in circumstances in which the with statement does not fit the needs
	# of the code.
	print("Will try to greet world ...")

	# creo un canale verso il server RPC
	with grpc.insecure_channel("localhost:50051") as channel: # non sicuro -> non crittografato
		
		# creo uno stub (GreeterStub, ovvero ${NOMESERVIZIO}Stub) per invocare tutti i metodi implementati nel servizio
		stub = helloworld_pb2_grpc.GreeterStub(channel)
		
		response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
		print("[CLIENT] SayHello invoked Greeter client received: " + response.message)

			
if __name__ == "__main__":
	run()
