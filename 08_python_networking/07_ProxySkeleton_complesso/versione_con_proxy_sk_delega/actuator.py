import sys
import threading as mt
import random
from datetime import datetime
from dispatcher_proxy import DispatcherProxy      


if __name__ == "__main__":

    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("Please, specify HOST/PORT args...")
        sys.exit(-1)

    cmd_dict = {0:"leggi", 1:"scrivi", 2:"configura", 3:"reset"}    
    i = 0
    
    while True:
        #Il programma principale inizia connettendosi al server dispatcher utilizzando il proxy DispatcherProxy.
        proxy = DispatcherProxy(HOST, int(PORT), mt.current_thread().name, i)
        #Utilizzando il metodo getCmd del proxy, l'attuatore richiede un comando al server dispatcher.
        data = proxy.getCmd()

        print(f'[ACTUATOR] received data for #{i} request: {data}...write to file\n')
        #Una volta ricevuto il comando, l'attuatore lo elabora, stampa le informazioni 
        # ricevute e scrive i dettagli del comando in un file di log 
        # denominato cmdLog.txt, insieme alla data e all'ora della ricezione del comando.
        with open("cmdLog.txt", mode="a") as cmdlog_file:
            cmdlog_file.write(f'{datetime.now()} {cmd_dict[int(data)]}\n')
        
        i = i + 1