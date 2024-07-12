import sys, stomp
    

if __name__ == "__main__":

    try:
            MSG = sys.argv[1]
    except IndexError:
            print("Please, specify MSG arg")

    #conn = stomp.Connection([('127.0.0.1', 61613)])
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False) # To use to send TextMessage to a JMS-based application
    
    """  L'opzione auto_content_length=False è utilizzata per evitare problemi 
    con JMS-based applications che potrebbero non gestire correttamente il 
    contenuto del messaggio se la lunghezza non è specificata automaticamente.
    """
    conn.connect(wait=True) # Stabilisce la connessione al broker STOMP e attende fino a quando la connessione non è completata.

    conn.send('/queue/test', MSG)
    
    print("Message: -", MSG, "- sent")

    conn.disconnect()
