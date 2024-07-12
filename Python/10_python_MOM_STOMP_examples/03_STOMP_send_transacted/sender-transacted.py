import sys, stomp
    

if __name__ == "__main__":

    try:
            MSG = sys.argv[1]
    except IndexError:
            print("Please, specify MSG arg")

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)

    # Avvia una nuova transazione STOMP e assegna l'ID della transazione a txid
    txid = conn.begin() # Start transaction
    

    for i in range(10):
        MSG_TO_SEND = MSG + "-" + str(i)
        conn.send('/topic/mytesttopic', MSG_TO_SEND, transaction=txid) # Send message in the transaction
        print("Message: -", MSG_TO_SEND, "- sent") 
    
    conn.commit(txid) # Commit transaction

    #conn.abort(txid) # Abort transaction, in modo da annullare gli invii fatti precedentemente
    
    

    conn.disconnect()
