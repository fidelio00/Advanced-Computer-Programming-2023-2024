

import java.net.*;

import javax.jms.JMSException;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueSender;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.jms.TextMessage;

import java.io.*;

public class ServiceProxy implements IService {
	
	private String addr;
	private int port;
	private QueueConnection qconnection;
	private Queue qresponse;
	
	
	public ServiceProxy ( String a, int p , QueueConnection qconnection, Queue qreponse){
		this.addr = new String ( a);
		this.port = p;	
		this.qconnection = qconnection;
		this.qresponse = qreponse;
	}
	
	
	public void deposita(int valore){
		
		try{
			Socket s = new Socket ( addr, port );
			
			System.out.println("[SERVICE_PROXY] deposita - Socket creata per comunicare con addr: " + addr +":" + port);

			DataOutputStream dataOut = new DataOutputStream ( s.getOutputStream() );
			
			/*  NOTE: A BufferedReader è utilizzato per invocare il metodo readLine, dal momento che le stringhe
			* 	generate lato Python sono terminate con \n, e lato Java la socket si aspetta il terminatore (di default Python non 
			* 	lo aggiunge)
			*/
			 BufferedReader dataIn = new BufferedReader(new InputStreamReader(s.getInputStream()));
			
			dataOut.writeUTF("deposita-" + valore);
			
			// forza il proxy ad attendere una risposta dal server
			// nel caso di metodo che restituisce void
			String result = dataIn.readLine();	

			System.out.println("[SERVICE_PROXY] deposita - result: " + result);
			
			s.close();

			// rispondo tramite JMS al client Python
			QueueSession qsession = qconnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
			TextMessage message = qsession.createTextMessage(result + "-" + valore);
			QueueSender sender = qsession.createSender(qresponse);
			sender.send(message);
		
		// da aggiungere per gestire problemi Proxy su socket
		}catch (UnknownHostException u ){
			u.printStackTrace();
		}catch (IOException e ){
			e.printStackTrace();
		
		// da aggiungere per gestire problemi JMS
		} catch (JMSException e) { 
			e.printStackTrace();
		}
		
	}
	
	
	public int preleva(){
		
		String x = null;
		
		try{
			
			Socket s = new Socket ( addr, port );
			
			DataOutputStream dataOut = new DataOutputStream ( s.getOutputStream() );
			
			/*  NOTE: A BufferedReader è utilizzato per invocare il metodo readLine, dal momento che le stringhe
			* 	generate lato Python sono terminate con \n, e lato Java la socket si aspetta il terminatore (di default Python non 
			* 	lo aggiunge)
			*/
			BufferedReader dataIn = new BufferedReader(new InputStreamReader(s.getInputStream()));
			
			dataOut.writeUTF("preleva");
			System.out.println("[SERVICE_PROXY] INVIATO MESSAGGIO di preleva SU SOCKET");
			
			x = new String(dataIn.readLine());
			
			System.out.println("[SERVICE_PROXY] Valore ricevuto: " + x);
			
			s.close();
		
			// rispondo tramite JMS al client Python
			QueueSession qsession = qconnection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
			TextMessage message = qsession.createTextMessage("Prelevato-" + x);
			QueueSender sender = qsession.createSender(qresponse);
			sender.send(message);

		}catch (UnknownHostException u ){
			u.printStackTrace();
		}catch (IOException e ){
			e.printStackTrace();
		} catch (JMSException e) {
			e.printStackTrace();
		}
		
		return Integer.valueOf(x);
	}
	

}
