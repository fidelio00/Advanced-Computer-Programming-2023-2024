### utilizzo della classe Event

import threading as thd
import time

#Definisce una funzione task che prende due parametri: 
# - event (un oggetto Event) 
# - timeout (il tempo massimo di attesa per l'evento).

def task(event, timeout):
   print("Started thread but waiting for event...")

   # make the thread wait for event with timeout set
   event_set = event.wait(timeout)

   if event_set:
     print("Event received, releasing thread...")
   else:
     print("Time out, moving ahead without event...")
    
if __name__ == '__main__':

    # initializing the event object
    e = thd.Event()
  
    # starting the thread
    thread = thd.Thread(name='Event-Thread', target=task, args=(e,4))
    thread.start()

    # sleeping the main thread for 3 seconds
    time.sleep(3)

    # generating the event
    e.set()
    print("Event is set.")

    # wait for the thread to complete
    thread.join()
    print("Event-Thread joined")
  

