import javax.jms.*;
import org.apache.activemq.ActiveMQConnectionFactory;

public class Sender {
    public static void main(String[] args) {
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = null;
        Session session = null;
        MessageProducer producer = null;
        
        try {
            // Creazione della connessione e della sessione
            connection = connectionFactory.createConnection();
            connection.start();
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            
            // Creazione della coda
            Destination destination = session.createQueue("testQueue");
            
            // Creazione del produttore di messaggi
            producer = session.createProducer(destination);
            
            // Creazione di un semplice messaggio di testo
            TextMessage message = session.createTextMessage("Questo è un messaggio di test!");
            
            // Invio del messaggio alla coda
            producer.send(message);
            
            System.out.println("Messaggio inviato con successo alla coda.");
        } catch (JMSException e) {
            e.printStackTrace();
        } finally {
            try {
                if (producer != null) {
                    producer.close();
                }
                if (session != null) {
                    session.close();
                }
                if (connection != null) {
                    connection.close();
                }
            } catch (JMSException e) {
                e.printStackTrace();
            }
        }
    }
}
