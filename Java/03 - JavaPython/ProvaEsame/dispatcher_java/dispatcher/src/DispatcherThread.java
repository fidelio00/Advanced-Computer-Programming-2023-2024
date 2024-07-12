import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.TextMessage;

public class DispatcherThread extends Thread{

    private int port;
    private QueueConnection qconnection;
    private TextMessage msg;
  
    //public DispatcherThread(int port, QueueConnection qconnection, Queue qresponse, TextMessage msg){
    public DispatcherThread(int port, QueueConnection qconnection, TextMessage msg){

        this.port = port;
        this.qconnection = qconnection;
        //this.qresponse = qresponse;
        this.msg = msg;

    }
    
    public void run(){
        try {

                String message = msg.getText(); // il messaggio ricevuto da STOMP è un TextMessage perchè ho settato auto_content_length=False per CONNECT
                
                System.out.println("[DISPATCHER_MSG_LISTENER] Messaggio ricevuto: " + message);
    
                System.out.println("[DISPATCHER_MSG_LISTENER] JMSReplyTo: " + msg.getJMSReplyTo());
                
                Queue qresponse = (Queue)msg.getJMSReplyTo();

                IService service_proxy = new ServiceProxy ("localhost", port, qconnection, qresponse); // creo un Proxy

                if(message.equalsIgnoreCase("preleva")){
                
                    // invoca il DispatcherProxy che deve invocare il servizio di prelievo
                    System.out.println("[DISPATCHER_MSG_LISTENER] Ricevuta richiesta prelievo");
                    
                    service_proxy.preleva();
                    
                }
                else if(message.contains("deposita")){

                    // Deposito
                    String[] splitted = message.split("-");
                    Integer valoreDaDepositare = Integer.valueOf(splitted[1]);
                    System.out.println("[DISPATCHER_MSG_LISTENER] Ricevuta richiesta di deposito. Valore da depositare " + valoreDaDepositare );
                    
                    // invoca il DispatcherProxy che deve invocare il servizio di deposito
                    service_proxy.deposita(valoreDaDepositare);
                }
            } catch (JMSException e) {
                e.printStackTrace();
        }
    }
}
